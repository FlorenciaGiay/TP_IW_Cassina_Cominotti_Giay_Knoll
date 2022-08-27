from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('entrepreneurs/', PostListView.as_view(), name='entrepreneurs'),
]