from django import forms
from .models import Event, Comment


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
        fields = ('user', 'content')
