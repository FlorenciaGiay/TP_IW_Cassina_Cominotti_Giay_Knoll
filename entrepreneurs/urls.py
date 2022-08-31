from django.urls import path
from .views import EntrepreneurListView , EntrepreneurDetailView

urlpatterns = [
    path('entrepreneurs/', EntrepreneurListView.as_view(), name='entrepreneurs'),
    path('entrepreneur/<int:pk>/', EntrepreneurDetailView.as_view(), name='entrepreneur-detail'),
]