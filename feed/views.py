import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_filters.views import FilterView
from django.views.generic import DetailView, CreateView, FormView, View
from feed.filter import EventFilter
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render, redirect
from feed.forms import EventUpdateForm, CommentForm
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse

from feed.models import Event, Comment, EventEntrepreneur, EventPetitionStatus
from entrepreneurs.models import Entrepreneur, EntrepreneurStatus


def home(request):
    return render(request, "feed/home.html")


def petitions(request):
    entrepreneur_profiles = Entrepreneur.objects.filter(status__description="Pendiente")
    event_petitions = EventEntrepreneur.objects.filter(status__description="Pendiente")
    context = {
        "entrepreneurs": entrepreneur_profiles,
        "event_petitions": event_petitions,
    }

    return render(request, "feed/petitions.html", context)


class EventListView(FilterView):
    paginate_by = 5
    ordering = ["-id"]
    template_name = "feed/event_home.html"
    model = Event
    filterset_class = EventFilter


class EventDisplay(DetailView):
    model = Event
    template_name = "feed/event_detail.html"
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        try:
            selected_event = kwargs.get("object")
            entrepreneur_already_participates = EventEntrepreneur.objects.get(
                event=selected_event, entrepreneur=self.request.user.entrepreneur
            )
        except Exception as e:
            entrepreneur_already_participates = None

        context["entrepreneur_already_participates"] = (
            entrepreneur_already_participates is not None
        )
        return context


@method_decorator(login_required, name="dispatch")
class PostComment(SingleObjectMixin, FormView):
    model = Event
    form_class = CommentForm
    template_name = "feed/event_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(self.request, *args, **kwargs)

    # def get_form_kwargs(self):
    #     kwargs = super(PostComment, self).get_form_kwargs()
    #     kwargs['request'] = self.request
    #     return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.event = self.object
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("event-detail", kwargs={"pk": post.pk}) + "#comments"


class EventDetailView(View):
    def get(self, request, *args, **kwargs):
        view = EventDisplay.as_view()
        return view(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(self.request, *args, **kwargs)


@method_decorator(login_required, name="dispatch")
class EventAddView(CreateView):
    model = Event
    template_name = "feed/event_add.html"
    fields = [
        "title",
        "content",
        "direction",
        "datetime_of_event",
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
            messages.success(request, f"El evento ha sido actualizado!")
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
