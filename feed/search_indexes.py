from haystack import indexes
from feed.models import Event

class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')
    direction = indexes.CharField(model_attr='direction')
    cost_of_entry = indexes.IntegerField(model_attr='cost_of_entry')
    created_at = indexes.DateTimeField(model_attr='created_at')
    datetime_of_event = indexes.DateTimeField(model_attr='datetime_of_event')

    def get_model(self):
        return Event

    def index_queryset(self, using=None):
        """ Used when entire index is updated """
        return self.get_model().objects.all()

