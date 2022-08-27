from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=False,
    )

    def __str__(self):
        return self.email
    class Role(models.TextChoices):
        CLIENT = "CLIENT", "Client"
        ENTREPRENEUR = "ENTREPRENEUR", "Entrepreneur"

    base_role = Role.CLIENT
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class ClientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENT)


class Client(User):
    base_role = User.Role.CLIENT
    client = ClientManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for clients"


@receiver(post_save, sender=Client)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CLIENT":
        ClientProfile.objects.create(user=instance)


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client_id = models.IntegerField(null=True, blank=True)
    # Add fields here for the Client Profile!