import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic import DetailView, CreateView
from feed.filter import EventFilter
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render, redirect
from feed.forms import EventUpdateForm

from feed.models import Event


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


@method_decorator(login_required, name="dispatch")
class EventAddView(CreateView):
    model = Event
    template_name = "feed/event_add.html"
    fields = [
        "title",
        "content",
        "direction",
        "cost_of_entry",
        "image_profile",
    ]

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return "/events/"


@login_required
def event_update_view(request, pk):
    event_selected = None
    try:
        event_selected = Event.objects.select_related().get(id=pk)
    except Event.DoesNotExist:
        pass

    if request.method == "POST":
        e_form = EventUpdateForm(request.POST, request.FILES, instance=event_selected)
        if e_form.is_valid():
            e_form.save()
            messages.success(request, f"Su cuenta ha sido actualizada!")
            return redirect("events")

    else:
        e_form = EventUpdateForm(instance=event_selected)

    context = {
        "e_form": e_form,
        "event": event_selected,
    }

    return render(request, "feed/event_update.html", context)


@login_required
def event_delete_view(request, pk=None):
    if request.method == "POST":
        event_to_delete = Event.objects.get(id=pk)
        event_to_delete.delete()
        return redirect("profile")

    if request.method == "GET":
        return render(
            request,
            "feed/event_confirm_delete.html",
            {"event_pk": pk},
        )
