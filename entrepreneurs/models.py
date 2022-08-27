from django.db import models
from users.models import User
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Entrepreneur(User):
#     entrepreneurship_name = models.CharField(max_length=100)
#     entrepreneurship_email = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=100)
#     description = models.TextField()
#     profile_status = models.ForeignKey('EntrepreneurStatus', null=True, blank=True, on_delete=models.SET_NULL)
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ForeignKey('EntrepreneurCategory', null=True, blank=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.name

# class EntrepreneurStatus(models.Model):
#     description = models.CharField(max_length=100)

#     def __str__(self):
#         return self.description

# class EntrepreneurCategory(models.Model):
#     description = models.CharField(max_length=100)

#     def __str__(self):
#         return self.description


class EntrepreneurManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ENTREPRENEUR)


class Entrepreneur(User):
    base_role = User.Role.ENTREPRENEUR
    entrepreneur = EntrepreneurManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for entrepreneurs"

    def __str__(self):
        return self.name


class EntrepreneurProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entrepreneur_id = models.IntegerField(null=True, blank=True)
    entrepreneurship_name = models.CharField(max_length=100)
    entrepreneurship_email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    description = models.TextField()
    # profile_status = models.ForeignKey('EntrepreneurStatus', null=True, blank=True, on_delete=models.SET_NULL)
    # category = models.ForeignKey('EntrepreneurCategory', null=True, blank=True, on_delete=models.SET_NULL)


@receiver(post_save, sender=Entrepreneur)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "ENTREPRENEUR":
        EntrepreneurProfile.objects.create(user=instance)
