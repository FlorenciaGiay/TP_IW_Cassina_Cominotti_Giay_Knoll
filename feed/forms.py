from django import forms
from .models import Event, Comment
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "content",
            "direction",
            "cost_of_entry",
            "image_profile",
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
