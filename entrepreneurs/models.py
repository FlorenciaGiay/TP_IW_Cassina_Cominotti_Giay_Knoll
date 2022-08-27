from django.db import models
from users.models import User

# Create your models here.
class Entrepreneur(User):
    entrepreneurship_name = models.CharField(max_length=100)
    entrepreneurship_email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    description = models.TextField()
    profile_status = models.ForeignKey('EntrepreneurStatus', null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('EntrepreneurCategory', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class EntrepreneurStatus(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class EntrepreneurCategory(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description