from django.urls import path
from .views import ProfileListView , EntrepreneurProfileDetailView

urlpatterns = [
    path('entrepreneurs/', ProfileListView.as_view(), name='entrepreneurs'),
    path('entrepreneur/<int:pk>/', EntrepreneurProfileDetailView.as_view(), name='entrepreneur-detail'),
]