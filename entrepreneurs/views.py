from asyncio import selector_events
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView
from django_filters.views import FilterView
from entrepreneurs.filter import EntrepreneurFilter
from entrepreneurs.forms import EntrepreneurUpdateForm, UserUpdateForm
from .models import Entrepreneur, EntrepreneurStatus
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail


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
                "user": request.user,
                "entrepreneur": entrepreneur,
                "domain": current_site.domain
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

        messages.info(request, f"El emprendedor {entrepreneur.entrepreneurship_email} ha sido aceptado")
    except Exception as e:
        messages.error(request, f"Falla al enviar el email de verificación.")

    return redirect("petitions")

def reject_entrepreneur_petition(request, pk):
    entrepreneur = Entrepreneur.objects.get(pk=pk)
    entrepreneur.status = EntrepreneurStatus.objects.get(description="Rechazado")
    entrepreneur.save()
    try:
        current_site = get_current_site(request)
        mail_subject = "Rafaela Emprende 💡 | Tu emprendimiento ha sido rechazado"
        message = render_to_string(
            "entrepreneurs/reject_entrepreneurship.html",
            {
                "user": request.user,
                "entrepreneur": entrepreneur,
                "domain": current_site.domain
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

        messages.info(request, f"El emprendedor {entrepreneur.entrepreneurship_email} ha sido rechazado")
    except Exception as e:
        messages.error(request, f"Falla al enviar el email de verificación.")

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
        if u_form.is_valid() and e_form.is_valid():
            u_form.save()
            e_form.save()
            messages.success(request, f"Su cuenta ha sido actualizada!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        e_form = EntrepreneurUpdateForm(instance=entrepreneur_selected)

    context = {
        "u_form": u_form,
        "e_form": e_form,
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
