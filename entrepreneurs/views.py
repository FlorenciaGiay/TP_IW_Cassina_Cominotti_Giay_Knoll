from django.shortcuts import render, redirect
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .forms import EntrepreneurRegisterForm
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.views.generic import ListView, DetailView
from .models import EntrepreneurProfile
from django.utils.decorators import method_decorator


emprendedores = [
    {
        'tipo': 'Artesanias',
        'nombre': 'Alondra',
        'content': 'Hago pulseras :)',
        'date_posted': datetime.datetime(2022, 8, 23, 7, 00, 00),
    },
    {
        'tipo': 'Gastronomia',
        'nombre': 'Mas chica la milanesa',
        'content': 'Hago comida :P',
        'date_posted': datetime.datetime(2022, 8, 23, 6, 00, 00),
    },
    {
        'tipo': 'Indumentaria',
        'nombre': 'Vestite bien',
        'content': 'Hago ropa XD',
        'date_posted': datetime.datetime(2022, 8, 22, 23, 00, 00),
    },
]

@login_required
def home(request):
    context = { 'emprendedores': emprendedores }
    return render(request, 'entrepreneurs/home.html', context)

@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):
    model = EntrepreneurProfile
    template_name = 'entrepreneurs/home.html'
    context_object_name = 'emprendedores'
    ordering = ['entrepreneurship_name']

@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = EntrepreneurProfile

def register(request):
    if request.method == 'POST':
        form = EntrepreneurRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            try:
                current_site = get_current_site(request)
                mail_subject = 'Rafaela Emprende 💡 | Active su cuenta'
                message = render_to_string('users/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = form.cleaned_data.get('email')

                send_mail(mail_subject,
                          '',
                          settings.EMAIL_HOST_USER,
                          [to_email],
                          fail_silently=True,
                          html_message=message)

                messages.success(
                    request, f'¡Su cuenta ha sido creada! Por favor, revise su bandeja de entrada y confirme su dirección de correo electrónico para completar el registro')
            except Exception as e:
                messages.error(
                    request, f'Falla al enviar el email de verificación.')

            return redirect('login')
    else:
        form = EntrepreneurRegisterForm()
    return render(request, 'entrepreneurs/register.html', {'form': form})
