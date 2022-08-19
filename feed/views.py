from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return render(request, 'feed/home.html')
  # return HTTPResponse('<h1>Hello Feed!!</h1>')
