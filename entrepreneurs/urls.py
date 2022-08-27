from django.urls import path
from . import views as entrepreneur_views

urlpatterns = [
    path('', entrepreneur_views.home, name='entrepreneurs'),
]