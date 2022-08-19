from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'¡Su cuenta ha sido creada! Ahora puede conectarse')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    default_image = 'https://pro2-bar-s3-cdn-cf.myportfolio.com/8ee9e0df6a57e6cb08ce8298364354c5/b4dd1698f1d995ddf6dc1caf45e69d0b5550752716af226bf5b6e140d0a48ae6175a3d2b28d2d24e_car_1x1.jpg?h=2f9a2d1908efc225350ee82423d2d7b5&url=aHR0cHM6Ly9taXItczMtY2RuLWNmLmJlaGFuY2UubmV0L3Byb2plY3RzL29yaWdpbmFsLzE5Yjg3YTI5Mjc0MzkzLjU1ZWFkMmU3MWFhNDMuanBn'
    image = request.user.profile.image.url if (hasattr(request.user, 'profile') and hasattr(request.user.profile, 'image') and hasattr(request.user.profile.image, 'url')) else default_image
    return render(request, 'users/profile.html', {'user_profile': image})
