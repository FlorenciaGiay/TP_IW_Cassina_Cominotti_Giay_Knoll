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
    entrepreneurship_name = models.CharField(
        max_length=100, verbose_name="Nombre del emprendimiento"
    )
    entrepreneurship_email = models.CharField(
        max_length=100, verbose_name="Email del emprendimiento"
    )
    phone_number = models.CharField(
        max_length=100, verbose_name="Número de teléfono del emprendimiento"
    )
    description = models.TextField(verbose_name="Descripción del emprendimiento")
    image_profile = models.ImageField(
        default="images/default.jpg",
        upload_to="images/entrepreneur_profile_pics",
        verbose_name="Foto de perfil del emprendimiento",
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


class EntrepreneurPhoto(models.Model):
    entrepreneur = models.ForeignKey(
        Entrepreneur, on_delete=models.CASCADE, related_name="photos"
    )
    image = models.ImageField(
        default="images/default.jpg", upload_to="images/entrepreneur_photos"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        output_size = (300, 300)
        img.thumbnail(output_size, Image.ANTIALIAS)
        # img = img.resize(output_size, Image.ANTIALIAS)
        img.save(self.image.path, quality=100, optimize=True)
