from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'author': 'Mauro Cominotti',
        'title': 'Blog Post 1',
        'content': 'Third post content',
        'date_posted': 'August 28, 2022'
    },
    {
        'author': 'Florencia Giay',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2022'
    },
    {
        'author': 'Paula Cassina',
        'title': 'Blog Post 3',
        'content': 'First post content',
        'date_posted': 'August 28, 2022'
    },
    {
        'author': 'Gonzalo Knoll',
        'title': 'Blog Post 4',
        'content': 'Second post content',
        'date_posted': 'August 28, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'feed/home.html', context)


def entrepreneurs(request):
    return render(request, 'feed/entrepreneurs.html')
