from django.urls import path
from .views import EntrepreneurListView, EntrepreneurDetailView, EntrepreneurAddView
from . import views as entrepreneur_views

urlpatterns = [
    path("entrepreneurs/", EntrepreneurListView.as_view(), name="entrepreneurs"),
    path("entrepreneur/add/", EntrepreneurAddView.as_view(), name="entrepreneur-add"),
    path(
        "entrepreneur/photo/add/",
        entrepreneur_views.entrepreneur_add_photos,
        name="entrepreneur-photos-add",
    ),
    path(
        "entrepreneur/photo/delete/<int:pk>/",
        entrepreneur_views.entrepreneur_delete_photos,
        name="entrepreneur-photos-delete",
    ),
    path(
        "entrepreneur/delete/<int:pk>",
        entrepreneur_views.entrepreneur_delete_view,
        name="entrepreneur-delete",
    ),
    path(
        "entrepreneur/update/<int:pk>/",
        entrepreneur_views.entrepreneur_update_view,
        name="entrepreneur-update",
    ),
    path(
        "entrepreneur/<int:pk>/",
        EntrepreneurDetailView.as_view(),
        name="entrepreneur-detail",
    ),
    path(
        "entrepreneur/accept-petition/<int:pk>/",
        entrepreneur_views.accept_entrepreneur_petition,
        name="accept-entrepreneur-petition",
    ),
    path(
        "entrepreneur/reject-petition/<int:pk>/",
        entrepreneur_views.reject_entrepreneur_petition,
        name="reject-entrepreneur-petition",
    ),
    path(
        "entrepreneur/make-event-petition/<int:event_pk>",
        entrepreneur_views.entrepreneur_make_event_petition,
        name="entrepreneur-make-event-petition",
    ),
    path(
        "entrepreneurship/accept-event-petition/<int:pk>/",
        entrepreneur_views.accept_entrepreneurship_event_petition,
        name="accept-entrepreneurship-event-petition",
    ),
    path(
        "entrepreneurship/reject-event-petition/<int:pk>/",
        entrepreneur_views.reject_entrepreneurship_event_petition,
        name="reject-entrepreneurship-event-petition",
    ),
]
