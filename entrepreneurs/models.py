from django.db import models
from users.models import User


class Entrepreneur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entrepreneurship_name = models.CharField(max_length=100)
    entrepreneurship_email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    description = models.TextField()
