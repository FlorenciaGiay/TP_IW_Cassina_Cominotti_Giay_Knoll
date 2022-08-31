from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Entrepreneur
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class EntrepreneurListView(ListView):
    paginate_by = 1
    template_name = 'entrepreneurs/home.html'
    model = Entrepreneur

@method_decorator(login_required, name='dispatch')
class EntrepreneurDetailView(DetailView):
    model = Entrepreneur
    template_name = 'entrepreneurs/entrepreneur_detail.html'
