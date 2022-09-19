from datetime import datetime
from django.db import models
from entrepreneurs.models import Entrepreneur
from users.models import User


class Event(models.Model):
    title = models.CharField(
        max_length=100, null=False, verbose_name="Título del evento"
    )
    content = models.TextField(null=False, verbose_name="Contenido del evento")
    direction = models.TextField(null=False, verbose_name="Dirección del evento")
    cost_of_entry = models.IntegerField(null=False, verbose_name="Costo de la entrada")
    created_at = models.DateTimeField(auto_now_add=True)
    datetime_of_event = models.DateTimeField(
        null=False, default=datetime.now, verbose_name="Fecha de Realización del evento"
    )
    image_profile = models.ImageField(
        default="images/default.jpg",
        upload_to="images/event_pics",
        verbose_name="Imagen de Perfil del evento",
    )

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return "Event {}".format(self.title)


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return "Comment {} by {}".format(self.content, self.user.email)


class EventPetitionStatus(models.Model):
    description = models.CharField(
        max_length=100,
        unique=True,
    )
    color = models.CharField(max_length=9, default="#17a2b8")

    def __str__(self):
        return self.description


class EventEntrepreneur(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        EventPetitionStatus,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        to_field="description",
        default="Pendiente",
    )
