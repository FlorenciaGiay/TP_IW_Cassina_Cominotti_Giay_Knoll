from django.db import models
from users.models import User
from PIL import Image


class EntrepreneurStatus(models.Model):
    description = models.CharField(max_length=100)
    color = models.CharField(max_length=9, default="#17a2b8")

    def __str__(self):
        return self.description


class EntrepreneurCategory(models.Model):
    description = models.CharField(max_length=100)
    color = models.CharField(max_length=9, default="#17a2b8")

    def __str__(self):
        return self.description

class Entrepreneur(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    entrepreneurship_name = models.CharField(max_length=100)
    entrepreneurship_email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    description = models.TextField()
    image_profile = models.ImageField(
        default="images/default.jpg", upload_to="images/entrepreneur_profile_pics"
    )
    status = models.ForeignKey(
        "EntrepreneurStatus", null=False, blank=False, on_delete=models.PROTECT
    )
    category = models.ForeignKey(
        "EntrepreneurCategory", null=False, blank=False, on_delete=models.PROTECT
    )
    number_of_attempts = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f"User.id: {self.user.id} - email: {self.user.email}"
