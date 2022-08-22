from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes #, force_text
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage  
import os


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user.is_active = False  
            user.save()  
            ######################### mail system ####################################
            # htmly = get_template('templates/Email.html')
            # d = {'username': username}
            # subject, from_email, to = 'Bienvenido a Rafaela Emprende!', os.environ.get(
            #     'EMAIL_HOST_USER'), email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(
            #     subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            ##################################################################

            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_active_email.html', {
                'user': username,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()

            messages.success(
                request, f'¡Su cuenta ha sido creada! Ahora puede conectarse')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    default_image = 'https://pro2-bar-s3-cdn-cf.myportfolio.com/8ee9e0df6a57e6cb08ce8298364354c5/b4dd1698f1d995ddf6dc1caf45e69d0b5550752716af226bf5b6e140d0a48ae6175a3d2b28d2d24e_car_1x1.jpg?h=2f9a2d1908efc225350ee82423d2d7b5&url=aHR0cHM6Ly9taXItczMtY2RuLWNmLmJlaGFuY2UubmV0L3Byb2plY3RzL29yaWdpbmFsLzE5Yjg3YTI5Mjc0MzkzLjU1ZWFkMmU3MWFhNDMuanBn'
    image = request.user.profile.image.url if (hasattr(request.user, 'profile') and hasattr(
        request.user.profile, 'image') and hasattr(request.user.profile.image, 'url')) else default_image
    return render(request, 'users/profile.html', {'user_profile': image})
