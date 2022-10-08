from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from entrepreneurs.models import Entrepreneur
from .forms import UserRegisterForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from users.models import User
from django.http import HttpResponse
from django.views.decorators.http import require_GET

UserModel = get_user_model()


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Sitemap: http://127.0.0.1:8000/sitemap.xml"
        if settings.DEBUG
        else "Sitemap: https://rafaela-emprende.herokuapp.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            try:
                current_site = get_current_site(request)
                mail_subject = "Rafaela Emprende 💡 | Active su cuenta"
                message = render_to_string(
                    "users/acc_active_email.html",
                    {
                        "user": user,
                        "domain": current_site.domain,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                    },
                )
                to_email = form.cleaned_data.get("email")

                send_mail(
                    mail_subject,
                    "",
                    f'"Rafaela Emprende Team" <{settings.EMAIL_HOST_USER}>',
                    [to_email],
                    fail_silently=True,
                    html_message=message,
                )

                messages.success(
                    request,
                    f"¡Su cuenta ha sido creada! Por favor, revise su bandeja de entrada y confirme su dirección de correo electrónico para completar el registro",
                )
            except Exception as e:
                messages.error(request, f"Falla al enviar el email de verificación.")

            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if (
        user is not None
        and default_token_generator.check_token(user, token)
        and not user.is_active
    ):
        user.is_active = True
        user.save()
        messages.success(
            request,
            f"Gracias por su confirmación por correo electrónico. Ya puede acceder a su cuenta.",
        )
    else:
        messages.error(request, f"El link de activación es invalido!")
    return redirect("login")


@login_required
def profile(request):
    entrepreneur_selected = None
    try:
        entrepreneur_selected = Entrepreneur.objects.select_related().get(
            user=request.user
        )
    except Entrepreneur.DoesNotExist:
        pass
    return render(
        request,
        "users/profile.html",
        {"entrepreneur": entrepreneur_selected},
    )


@login_required
def user_delete_view(request):
    user_to_delete = request.user

    try:
        entrepreneur_selected = Entrepreneur.objects.select_related().get(
            user=user_to_delete
        )
    except Entrepreneur.DoesNotExist:
        pass

    try:
        user_to_delete = User.objects.select_related().get(pk=user_to_delete.pk)
        user_to_delete.delete()
        messages.success(request, f"Su cuenta ha sido eliminada")
        return redirect("login")
    except Entrepreneur.DoesNotExist:
        messages.error(
            request,
            f"Hubo un error al eliminar su cuenta. Por favor intentelo de nuevo más tarde",
        )
        return render(
            request,
            "users/profile.html",
            {"entrepreneur": entrepreneur_selected},
        )
