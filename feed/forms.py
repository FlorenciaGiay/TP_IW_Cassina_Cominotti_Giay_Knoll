from django import forms
from .models import Event, Comment


class EventFilterForm(forms.ModelForm):
    text_search = forms.CharField(required=False, label="Búsqueda por texto")
    cost_of_entry_min = forms.IntegerField(required=False, label="Costo de Minimo")
    cost_of_entry_max = forms.IntegerField(required=False, label="Costo de Máximo")
    datetime_from_event = forms.DateTimeField(
        label="Fecha desde",
        input_formats=["%d/%m/%Y %H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#datetimepicker_filterevent_fromevent",
            }
        ),
        required=False,
    )
    datetime_to_event = forms.DateTimeField(
        label="Fecha hasta",
        input_formats=["%d/%m/%Y %H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#datetimepicker_filterevent_toevent",
            }
        ),
        required=False,
    )

    class Meta:
        model = Event
        fields = [
            "text_search",
            "cost_of_entry_min",
            "cost_of_entry_max",
            "datetime_from_event",
            "datetime_to_event",
        ]


class EventAddForm(forms.ModelForm):
    datetime_of_event = forms.DateTimeField(
        label="Fecha de realización",
        input_formats=["%d/%m/%Y %H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#datetimepicker_addevent",
            }
        ),
    )

    class Meta:
        model = Event
        fields = [
            "title",
            "content",
            "direction",
            "cost_of_entry",
            "datetime_of_event",
            "image_profile"
        ]


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "content",
            "direction",
            "cost_of_entry",
            "image_profile",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
