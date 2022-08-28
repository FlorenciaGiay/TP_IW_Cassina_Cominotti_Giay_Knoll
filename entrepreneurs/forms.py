from django import forms
from entrepreneurs.models import Entrepreneur
from django.contrib.auth.forms import UserCreationForm


class EntrepreneurRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Entrepreneur
        fields = ['username', 'email', 'password1', 'password2']