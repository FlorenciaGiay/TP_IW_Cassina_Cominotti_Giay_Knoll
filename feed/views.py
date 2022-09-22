from datetime import datetime
from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic import DetailView, CreateView, FormView, View, ListView
from feed.filter import EventFilter
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render, redirect
from feed.forms import EventAddForm, EventFilterForm, EventUpdateForm, CommentForm
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from feed.models import Event, EventEntrepreneur
from entrepreneurs.models import Entrepreneur
from django.db.models import Q
from django.conf import settings
from django.utils.timezone import make_aware
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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


# class EventListView(FilterView):
#     queryset = Event.objects.exclude(datetime_of_event__lt=datetime.now())
#     paginate_by = 5
#     ordering = ["-datetime_of_event"]
#     template_name = "feed/event_home.html"
#     model = Event
#     filterset_class = EventFilter

class EventListView(ListView):
    paginate_by = 2
    template_name = "feed/event_home.html"
    model = Event
    form_class = EventFilterForm

    def get(self, request, *args, **kwargs):
        filter_form = self.form_class(request.GET)

        # Get the parameters from the body of the request
        title = request.GET.get("title")
        cost_of_entry = request.GET.get("cost_of_entry")
        datetime_from_event = request.GET.get("datetime_from_event")
        datetime_to_event = request.GET.get("datetime_to_event")
        values = {
            "title": title,
            "cost_of_entry": cost_of_entry,
            "datetime_from_event": datetime_from_event,
            "datetime_to_event": datetime_to_event
        }

        # Create the query to make to the database
        Qr = None
        if len(values) != 0:
            for key, value in values.items():
                if value == '' or value is None:
                    continue

                q = Q(**{"%s" % key: value })

                if key == "datetime_from_event":
                    q = Q(datetime_of_event__gt=datetime.strptime(value, "%d/%m/%Y %H:%M"))

                if key == "datetime_to_event":
                    q = Q(datetime_of_event__lt=datetime.strptime(value, "%d/%m/%Y %H:%M"))

                if Qr:
                    Qr = Qr & q # or | for filtering
                else:
                    Qr = q

        if Qr:
            event_list = Event.objects.filter(Qr).order_by("datetime_of_event")
        else:
            event_list = Event.objects.exclude(datetime_of_event__lt=datetime.now()).order_by("datetime_of_event")

        ########################### Pagination ###########################
        paginator = Paginator(event_list, request.GET.get('paginate_by', 3))
        page = request.GET.get('page')

        try:
            paginated = paginator.page(page)
        except PageNotAnInteger:
            paginated = paginator.page(1)
        except EmptyPage:
            paginated = paginator.page(paginator.num_pages)
        ########################### Pagination ###########################

        settings.TIME_ZONE
        datetime_now = make_aware(datetime.now())
        return render(request, self.template_name, {'page_obj':paginated, 'paginate_by': request.GET.get('paginate_by', 3), 'filter_form': filter_form, "event_list": paginated.object_list, "datetime_now": datetime_now})

class EventDisplay(DetailView):
    model = Event
    template_name = "feed/event_detail.html"
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        selected_event = kwargs.get("object")
        try:
            entrepreneur_already_participates = EventEntrepreneur.objects.get(
                event=selected_event, entrepreneur=self.request.user.entrepreneur
            )
        except Exception as e:
            entrepreneur_already_participates = None

        try:
            participant_petitions = EventEntrepreneur.objects.filter(
                event=selected_event, status__description="Aprobado"
            )
        except Exception as e:
            participant_petitions = None

        context["entrepreneur_already_participates"] = (
            entrepreneur_already_participates is not None
        )
        context["participant_petitions"] = participant_petitions
        return context


@method_decorator(login_required, name="dispatch")
class PostComment(SingleObjectMixin, FormView):
    model = Event
    form_class = CommentForm
    template_name = "feed/event_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(self.request, *args, **kwargs)

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
    form_class = EventAddForm

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
