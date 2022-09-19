from django import forms
from .models import Event, Comment
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.forms import DateTimeInput


class EventAddForm(forms.ModelForm):
    datetime_of_event = forms.DateTimeField(
        label="Fecha de realización",
        input_formats=["%d/%m/%Y %H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#datetimepicker_addevent",
            }
        ),
    )

    class Meta:
        model = Event
        fields = [
            "title",
            "content",
            "direction",
            "cost_of_entry",
            "image_profile",
            "datetime_of_event",
        ]


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
        fields = [
            "content",
        ]
