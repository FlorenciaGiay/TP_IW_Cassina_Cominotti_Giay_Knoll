import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic import DetailView, CreateView
from feed.filter import EventFilter

from feed.models import Event


def home(request):
    return render(request, "feed/home.html")

class EventListView(FilterView):
    paginate_by = 5
    ordering = ["-id"]
    template_name = "feed/event_home.html"
    model = Event
    filterset_class = EventFilter

class EventDetailView(DetailView):
    model = Event
    template_name = "feed/event_detail.html"