from django_filters import FilterSet
from .models import Event


class EventFilter(FilterSet):
    class Meta:
        model = Event
        fields = ["created_at"]
