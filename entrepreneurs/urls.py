from django.urls import path
from .views import EntrepreneurListView, EntrepreneurDetailView, EntrepreneurAddView
from . import views as entrepreneur_views

urlpatterns = [
    path("entrepreneurs/", EntrepreneurListView.as_view(), name="entrepreneurs"),
    path("entrepreneur/add/", EntrepreneurAddView.as_view(), name="entrepreneur-add"),
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
        "entrepreneur/accept-petition/<int:pk>/",
        entrepreneur_views.reject_entrepreneur_petition,
        name="reject-entrepreneur-petition",
    ),
]
