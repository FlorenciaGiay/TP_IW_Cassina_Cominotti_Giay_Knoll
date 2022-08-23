import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


posts = [
    {
        'author': 'Mauro Cominotti',
        'title': 'Post 1',
        'content': 'Third post content',
        'date_posted': datetime.datetime(2022, 8, 23, 7, 00, 00),
    },
    {
        'author': 'Florencia Giay',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': datetime.datetime(2022, 8, 23, 6, 00, 00),
    },
    {
        'author': 'Paula Cassina',
        'title': 'Post 3',
        'content': 'First post content',
        'date_posted': datetime.datetime(2022, 8, 22, 23, 00, 00),
    },
    {
        'author': 'Gonzalo Knoll',
        'title': 'Post 4',
        'content': 'Second post content',
        'date_posted': datetime.datetime(2022, 8, 22, 22, 00, 00),
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'feed/home.html', context)

@login_required
def entrepreneurs(request):
    return render(request, 'feed/entrepreneurs.html')
