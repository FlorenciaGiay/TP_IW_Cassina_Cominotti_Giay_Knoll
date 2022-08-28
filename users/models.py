from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=False,
    )

    def __str__(self):
        return f"Role: {self.role} - Email: {self.email}"
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CLIENT = "CLIENT", "Client"
        ENTREPRENEUR = "ENTREPRENEUR", "Entrepreneur"

        def __str__(self):
            return self.value

    base_role = Role.CLIENT
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.CLIENT)

class ClientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENT)


class Client(User):
    base_role = User.Role.CLIENT
    client = ClientManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client_id = models.IntegerField(null=True, blank=True)
    # Add fields here for the Client Profile!