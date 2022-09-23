from asyncio import selector_events
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView
from django_filters.views import FilterView
from entrepreneurs.filter import EntrepreneurFilter
from entrepreneurs.forms import (
    EntrepreneurUpdateForm,
    UserUpdateForm,
    EntrepreneurImageForm,
)
from feed.models import Event, EventEntrepreneur, EventPetitionStatus
from .models import Entrepreneur, EntrepreneurStatus, EntrepreneurPhoto
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers


class EntrepreneurListView(FilterView):
    paginate_by = 5
    ordering = ["-id"]
    template_name = "entrepreneurs/home.html"
    model = Entrepreneur
    filterset_class = EntrepreneurFilter


class EntrepreneurDetailView(DetailView):
    model = Entrepreneur
    template_name = "entrepreneurs/entrepreneur_detail.html"


def accept_entrepreneur_petition(request, pk):
    entrepreneur = Entrepreneur.objects.get(pk=pk)
    entrepreneur.status = EntrepreneurStatus.objects.get(description="Activo")
    entrepreneur.save()
    try:
        current_site = get_current_site(request)
        mail_subject = "Rafaela Emprende 💡 | Tu emprendimiento ha sido aprobado!"
        message = render_to_string(
            "entrepreneurs/accept_entrepreneurship.html",
            {
                "user": entrepreneur.user,
                "entrepreneur": entrepreneur,
                "domain": current_site.domain,
            },
        )
        to_email = entrepreneur.user.email

        send_mail(
            mail_subject,
            "",
            f'"Rafaela Emprende Team" <{settings.EMAIL_HOST_USER}>',
            [to_email],
            fail_silently=True,
            html_message=message,
        )

        messages.info(
            request,
            f"El emprendedor {entrepreneur.entrepreneurship_email} ha sido aceptado",
        )
    except Exception as e:
        messages.error(request, f"Falla al enviar el email")

    return redirect("petitions")


def reject_entrepreneur_petition(request, pk):
    entrepreneur = Entrepreneur.objects.get(pk=pk)
    entrepreneur.status = EntrepreneurStatus.objects.get(description="Rechazado")
    entrepreneur.number_of_attempts = entrepreneur.number_of_attempts + 1
    if (
        entrepreneur.number_of_attempts
        <= settings.NUMBER_OF_ATTEMPTS_TO_CREATE_ENTREPRENEUR_PROFILE
    ):
        entrepreneur.save()
    else:
        # Delete entrepreneurship completely
        Entrepreneur.delete(pk=entrepreneur.pk)

        # Send email noticing the complete delete of the entrepreneur profile
        current_site = get_current_site(request)
        mail_subject = "Rafaela Emprende 💡 | Tu emprendimiento ha sido rechazado"
        message = render_to_string(
            "entrepreneurs/reject_completely_entrepreneur_petition.html",
            {
                "user": entrepreneur.user,
                "entrepreneur": entrepreneur,
                "domain": current_site.domain,
            },
        )
        to_email = request.user.email

        send_mail(
            mail_subject,
            "",
            f'"Rafaela Emprende Team" <{settings.EMAIL_HOST_USER}>',
            [to_email],
            fail_silently=True,
            html_message=message,
        )

        messages.info(
            request,
            f"El emprendedor {entrepreneur.entrepreneurship_email} ha sido rechazado completamente por pasar el límite de intentos de verificación",
        )

    try:
        current_site = get_current_site(request)
        mail_subject = "Rafaela Emprende 💡 | Tu emprendimiento ha sido rechazado"
        message = render_to_string(
            "entrepreneurs/reject_entrepreneurship.html",
            {
                "user": entrepreneur.user,
                "entrepreneur": entrepreneur,
                "domain": current_site.domain,
            },
        )
        to_email = request.user.email

        send_mail(
            mail_subject,
            "",
            f'"Rafaela Emprende Team" <{settings.EMAIL_HOST_USER}>',
            [to_email],
            fail_silently=True,
            html_message=message,
        )

        messages.info(
            request,
            f"El emprendedor {entrepreneur.entrepreneurship_email} ha sido rechazado",
        )
    except Exception as e:
        messages.error(request, f"Falla al enviar el email")

    return redirect("petitions")


def entrepreneur_make_event_petition(request, event_pk):
    selected_entrepreneur = Entrepreneur.objects.get(user=request.user)
    try:
        selected_event = Event.objects.get(pk=event_pk)
        entrepreneur_already_participates = EventEntrepreneur.objects.get(
            event=selected_event, entrepreneur=selected_entrepreneur
        )
    except Exception as e:
        entrepreneur_already_participates = None
    if (
        selected_entrepreneur is None
        or selected_event is None
        or entrepreneur_already_participates
    ):
        messages.error(request, f"Falla al subscribirse al evento")
        return reverse("event-detail", kwargs={"pk": selected_event.pk})

    # Create new EventEntrepreneur
    pending_petition_status = EventPetitionStatus.objects.get(description="Pendiente")
    new_petition = EventEntrepreneur(
        event=selected_event,
        entrepreneur=selected_entrepreneur,
        status=pending_petition_status,
    )
    new_petition.save()

    try:
        current_site = get_current_site(request)
        mail_subject = (
            f"Rafaela Emprende 💡 | Te has suscrito al evento '{selected_event.title}'!"
        )
        message = render_to_string(
            "entrepreneurs/petition_to_event.html",
            {
                "user": request.user,
                "event": selected_event,
                "domain": current_site.domain,
            },
        )
        to_email = request.user.email

        send_mail(
            mail_subject,
            "",
            f'"Rafaela Emprende Team" <{settings.EMAIL_HOST_USER}>',
            [to_email],
            fail_silently=True,
            html_message=message,
        )

        messages.info(
            request,
            f"Tu petición para participar del evento {selected_event.title} ha sido enviada",
        )
    except Exception as e:
        messages.error(request, f"Falla al enviar petición para participar en evento.")

    return HttpResponseRedirect(
        reverse("event-detail", kwargs={"pk": selected_event.pk})
    )


def accept_entrepreneurship_event_petition(request, pk):
    petition = EventEntrepreneur.objects.get(pk=pk)
    entrepreneur = petition.entrepreneur
    petition.status = EventPetitionStatus.objects.get(description="Aprobado")
    petition.save()
    try:
        current_site = get_current_site(request)
        mail_subject = "Rafaela Emprende 💡 | Tu petición al evento ha sido aprobada!"
        message = render_to_string(
            "entrepreneurs/accept_entrepreneur_petition.html",
            {
                "user": entrepreneur.user,
                "entrepreneur": entrepreneur,
                "event": petition.event,
                "domain": current_site.domain,
            },
        )
        to_email = entrepreneur.user.email

        send_mail(
            mail_subject,
            "",
            f'"Rafaela Emprende Team" <{settings.EMAIL_HOST_USER}>',
            [to_email],
            fail_silently=True,
            html_message=message,
        )

        messages.info(
            request,
            f"La petición del emprendedor {entrepreneur.entrepreneurship_email} para el evento {petition.event.title} ha sido aprobada",
        )
    except Exception as e:
        messages.error(request, f"Falla al enviar el email")

    return redirect("petitions")


def reject_entrepreneurship_event_petition(request, pk):
    petition = EventEntrepreneur.objects.get(pk=pk)
    entrepreneur = petition.entrepreneur
    petition.status = EventPetitionStatus.objects.get(description="Rechazado")
    petition.save()
    try:
        current_site = get_current_site(request)
        mail_subject = "Rafaela Emprende 💡 |  Tu petición al evento ha sido rechazada"
        message = render_to_string(
            "entrepreneurs/reject_entrepreneur_petition.html",
            {
                "user": entrepreneur.user,
                "entrepreneur": entrepreneur,
                "event": petition.event,
                "domain": current_site.domain,
            },
        )
        to_email = entrepreneur.user.email

        send_mail(
            mail_subject,
            "",
            f'"Rafaela Emprende Team" <{settings.EMAIL_HOST_USER}>',
            [to_email],
            fail_silently=True,
            html_message=message,
        )

        messages.info(
            request,
            f"La petición del emprendedor {entrepreneur.entrepreneurship_email} para el evento {petition.event.title} ha sido rechazada",
        )
    except Exception as e:
        messages.error(request, f"Falla al enviar el email")

    return redirect("petitions")


@method_decorator(login_required, name="dispatch")
class EntrepreneurAddView(CreateView):
    model = Entrepreneur
    template_name = "entrepreneurs/entrepreneur_add.html"
    fields = [
        "entrepreneurship_name",
        "entrepreneurship_email",
        "phone_number",
        "description",
        "category",
    ]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        status = EntrepreneurStatus.objects.get(description="Pendiente")
        self.object.status = status
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return "/profile/"


@login_required
def entrepreneur_update_view(request, pk):
    entrepreneur_selected = None
    try:
        entrepreneur_selected = Entrepreneur.objects.select_related().get(
            user=request.user
        )
    except Entrepreneur.DoesNotExist:
        pass

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        e_form = EntrepreneurUpdateForm(
            request.POST, request.FILES, instance=entrepreneur_selected
        )
        files = request.FILES.getlist("image")
        if u_form.is_valid() and e_form.is_valid():
            u_form.save()
            e_form.save()
            for i in files:
                EntrepreneurPhoto.objects.create(
                    entrepreneur=entrepreneur_selected, image=i
                )
            messages.success(request, f"Su cuenta ha sido actualizada!")

            if entrepreneur_selected.status.description == "Rechazado":
                entrepreneur_selected.status = EntrepreneurStatus.objects.get(
                    description="Pendiente"
                )

            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        e_form = EntrepreneurUpdateForm(instance=entrepreneur_selected)
        photos_selected = EntrepreneurPhoto.objects.filter(
            entrepreneur=entrepreneur_selected
        ).first()
        i_form = (
            EntrepreneurImageForm(instance=photos_selected)
            if photos_selected
            else EntrepreneurImageForm()
        )

    context = {
        "u_form": u_form,
        "e_form": e_form,
        "i_form": i_form,
        "entrepreneur": entrepreneur_selected,
    }

    return render(request, "entrepreneurs/entrepreneur_update.html", context)


@login_required
def entrepreneur_delete_view(request, pk=None):
    if request.method == "POST":
        entrepreneur_to_delete = Entrepreneur.objects.get(id=pk)
        entrepreneur_to_delete.delete()
        return redirect("profile")

    if request.method == "GET":
        return render(
            request,
            "entrepreneurs/entrepreneur_confirm_delete.html",
            {"entrepreneur_pk": pk},
        )


@login_required
def entrepreneur_add_photos(request, pk=None):
    if request.method == "POST":
        try:
            entrepreneur_selected = None
            try:
                entrepreneur_selected = Entrepreneur.objects.select_related().get(
                    user=request.user
                )
            except Entrepreneur.DoesNotExist:
                return JsonResponse(status=404, data={"message":"Hubo un problema al cargar la Foto"})

            file = request.FILES.getlist("file")
            entrepreneur_photo_to_add = EntrepreneurPhoto.objects.create(
                    entrepreneur=entrepreneur_selected, image=file[0]
                )
            image_url = request.build_absolute_uri(entrepreneur_photo_to_add.image.url)
            serialized_entrepreneur_photo = serializers.serialize('json', [entrepreneur_photo_to_add, ])
            return JsonResponse(status=200, data={"message":"La foto del emprendedor fue cargada exitosamente", "entrepreneurPhoto": serialized_entrepreneur_photo,  "entrepreneurPhotoUrl": image_url})
        except EntrepreneurPhoto.DoesNotExist:
            return JsonResponse(status=404, data={"message":"Hubo un problema al cargar la Foto"})

@login_required
def entrepreneur_delete_photos(request, pk=None):
    if request.method == "DELETE":
        try:
            entrepreneur_photo_to_delete = EntrepreneurPhoto.objects.get(id=pk)
            entrepreneur_photo_to_delete.delete()
            return JsonResponse(status=200, data={"message":"La foto del emprendedor fue borrada exitosamente"})
        except EntrepreneurPhoto.DoesNotExist:
            return JsonResponse(status=404, data={"message":"Hubo un problema al eliminar la Foto"})
