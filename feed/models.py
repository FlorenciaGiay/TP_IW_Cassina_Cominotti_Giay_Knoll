from django.db import models
from entrepreneurs.models import Entrepreneur
from users.models import User


class Event(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    direction = models.TextField(null=False)
    cost_of_entry = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image_profile = models.ImageField(
        default="images/default.jpg", upload_to="images/event_pics"
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
        ordering = ["created_at"]

    def __str__(self):
        return "Comment {} by {}".format(self.content, self.user.email)


class EventEntrepreneur(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
