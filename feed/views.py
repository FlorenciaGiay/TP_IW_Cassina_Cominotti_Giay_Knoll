import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_filters.views import FilterView
from django.views.generic import DetailView, CreateView
from feed.filter import EventFilter
from .forms import CommentForm

from feed.models import Event, Comment


def home(request):
    return render(request, "feed/home.html")

class EventListView(FilterView):
    paginate_by = 5
    ordering = ["-id"]
    template_name = "feed/event_home.html"
    model = Event
    filterset_class = EventFilter

class EventDetailView(DetailView):
    model = Event
    template_name = "feed/event_detail.html"

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})