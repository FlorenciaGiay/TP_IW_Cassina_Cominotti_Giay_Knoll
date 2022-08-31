from django.db import models
from users.models import User


class EntrepreneurStatus(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class EntrepreneurCategory(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Entrepreneur(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    entrepreneurship_name = models.CharField(max_length=100)
    entrepreneurship_email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey('EntrepreneurStatus', null=False, blank=False, on_delete=models.PROTECT)
    category = models.ForeignKey('EntrepreneurCategory', null=False, blank=False, on_delete=models.PROTECT)
