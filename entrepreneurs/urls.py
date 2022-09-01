from django.urls import path
from .views import EntrepreneurListView , EntrepreneurDetailView, EntrepreneurAddView

urlpatterns = [
    path('entrepreneurs/', EntrepreneurListView.as_view(), name='entrepreneurs'),
    path('entrepreneur/add/', EntrepreneurAddView.as_view(), name='entrepreneur-add'),
    path('entrepreneur/<int:pk>/', EntrepreneurDetailView.as_view(), name='entrepreneur-detail'),
]