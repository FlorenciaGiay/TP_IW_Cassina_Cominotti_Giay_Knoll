from django.urls import path
from .views import EntrepreneurListView , EntrepreneurDetailView, EntrepreneurAddView
from . import views as entrepreneur_views

urlpatterns = [
    path('entrepreneurs/', EntrepreneurListView.as_view(), name='entrepreneurs'),
    path('entrepreneur/add/', EntrepreneurAddView.as_view(), name='entrepreneur-add'),
    path('entrepreneur/update/<int:pk>/', entrepreneur_views.entrepreneur_update_view, name='entrepreneur-update'),
    path('entrepreneur/<int:pk>/', EntrepreneurDetailView.as_view(), name='entrepreneur-detail'),
]