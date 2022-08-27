from django.shortcuts import render
from django.views.generic import ListView
from .models import Entrepreneur

# Create your views here.
class PostListView(ListView):
    model = Entrepreneur