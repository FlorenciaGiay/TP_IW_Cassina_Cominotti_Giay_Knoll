from django_filters import FilterSet
from .models import Event
from django import forms


class EventFilter(FilterSet):
    class Meta:
        model = Event
        fields = ["title", "cost_of_entry"]
