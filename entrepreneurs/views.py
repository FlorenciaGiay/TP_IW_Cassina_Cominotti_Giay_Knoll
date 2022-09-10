from asyncio import selector_events
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView
from django_filters.views import FilterView
from entrepreneurs.filter import EntrepreneurFilter
from entrepreneurs.forms import EntrepreneurUpdateForm, UserUpdateForm
from .models import Entrepreneur, EntrepreneurStatus
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages


class EntrepreneurListView(FilterView):
    paginate_by = 5
    ordering = ["-id"]
    template_name = "entrepreneurs/home.html"
    model = Entrepreneur
    filterset_class = EntrepreneurFilter


class EntrepreneurDetailView(DetailView):
    model = Entrepreneur
    template_name = "entrepreneurs/entrepreneur_detail.html"


@method_decorator(login_required, name="dispatch")
class EntrepreneurAddView(CreateView):
    model = Entrepreneur
    template_name = "entrepreneurs/entrepreneur_add.html"
    fields = [
        "entrepreneurship_name",
        "entrepreneurship_email",
        "phone_number",
        "description",
        "category",
    ]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        status = EntrepreneurStatus.objects.get(description="Pendiente")
        self.object.status = status
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return "/profile/"


@login_required
def entrepreneur_update_view(request, pk):
    entrepreneur_selected = None
    try:
        entrepreneur_selected = Entrepreneur.objects.select_related().get(
            user=request.user
        )
    except Entrepreneur.DoesNotExist:
        pass

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        e_form = EntrepreneurUpdateForm(
            request.POST, request.FILES, instance=entrepreneur_selected
        )
        if u_form.is_valid() and e_form.is_valid():
            u_form.save()
            e_form.save()
            messages.success(request, f"Su cuenta ha sido actualizada!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        e_form = EntrepreneurUpdateForm(instance=entrepreneur_selected)

    context = {
        "u_form": u_form,
        "e_form": e_form,
        "entrepreneur": entrepreneur_selected,
    }

    return render(request, "entrepreneurs/entrepreneur_update.html", context)


@login_required
def entrepreneur_delete_view(request, pk=None):
    if request.method == "POST":
        entrepreneur_to_delete = Entrepreneur.objects.get(id=pk)
        entrepreneur_to_delete.delete()
        return redirect("profile")

    if request.method == "GET":
        return render(
            request,
            "entrepreneurs/entrepreneur_confirm_delete.html",
            {"entrepreneur_pk": pk},
        )


@login_required
def events(request):
    return render(request, "entrepreneurs/events.html")
