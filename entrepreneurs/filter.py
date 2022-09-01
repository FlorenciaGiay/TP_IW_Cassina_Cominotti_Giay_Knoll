from django_filters import FilterSet
from .models import Entrepreneur


class EntrepreneurFilter(FilterSet):
    class Meta:
        model = Entrepreneur
        fields = ["category"]
