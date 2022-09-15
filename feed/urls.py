from django.urls import path
from .views import EventListView, EventDetailView, EventAddView
from . import views as event_views


urlpatterns = [
    path("", event_views.home, name="feed-home"),
    path("events/", EventListView.as_view(), name="events"),
    path("event/add/", EventAddView.as_view(), name="event-add"),
    path(
        "event/delete/<int:pk>",
        event_views.event_delete_view,
        name="event-delete",
    ),
    path(
        "event/update/<int:pk>/",
        event_views.event_update_view,
        name="event-update",
    ),
    path(
        "event/<int:pk>/",
        EventDetailView.as_view(),
        name="event-detail",
    ),
    path(
        "petitions",
        event_views.petitions,
        name="petitions",
    ),
]
