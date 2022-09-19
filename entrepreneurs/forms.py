from django import forms
from users.models import User
from .models import Entrepreneur, EntrepreneurPhoto


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class EntrepreneurUpdateForm(forms.ModelForm):
    class Meta:
        model = Entrepreneur
        fields = [
            "entrepreneurship_name",
            "entrepreneurship_email",
            "phone_number",
            "description",
            "category",
            "image_profile",
        ]


class EntrepreneurImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Fotos del Emprendimiento",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )

    class Meta:
        model = EntrepreneurPhoto
        fields = ("image",)
