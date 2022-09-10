from django.urls import path
from . import views
from .views import EventListView, EventDetailView


urlpatterns = [
    path("", views.home, name="feed-home"),
    path("events/", EventListView.as_view(), name="events"),
        path(
        "event/<int:pk>/",
        EventDetailView.as_view(),
        name="event-detail",
    ),
]
