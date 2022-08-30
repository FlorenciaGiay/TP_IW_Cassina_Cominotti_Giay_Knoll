from django.urls import path
from . import views as entrepreneur_views
from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path('', ProfileListView.as_view(), name='entrepreneurs'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]