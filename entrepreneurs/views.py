from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView
from django_filters.views import FilterView
from entrepreneurs.filter import EntrepreneurFilter
from .models import Entrepreneur, EntrepreneurStatus
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect


@method_decorator(login_required, name='dispatch')
class EntrepreneurListView(FilterView):
    paginate_by = 1
    ordering = ["-id"]
    template_name = 'entrepreneurs/home.html'
    model = Entrepreneur
    filterset_class = EntrepreneurFilter

@method_decorator(login_required, name='dispatch')
class EntrepreneurDetailView(DetailView):
    model = Entrepreneur
    template_name = 'entrepreneurs/entrepreneur_detail.html'

@method_decorator(login_required, name='dispatch')
class EntrepreneurAddView(CreateView):
    model = Entrepreneur
    template_name = 'entrepreneurs/entrepreneur_add.html'
    fields = ["entrepreneurship_name", "entrepreneurship_email", "phone_number", "description", "category"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        status = EntrepreneurStatus.objects.get(description="Pendiente")
        self.object.status = status
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return '/profile/'
