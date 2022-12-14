# Generated by Django 4.1 on 2022-09-19 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("entrepreneurs", "0003_entrepreneur_number_of_attempts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entrepreneur",
            name="description",
            field=models.TextField(verbose_name="Descripción del emprendimiento"),
        ),
        migrations.AlterField(
            model_name="entrepreneur",
            name="entrepreneurship_email",
            field=models.CharField(
                max_length=100, verbose_name="Email del emprendimiento"
            ),
        ),
        migrations.AlterField(
            model_name="entrepreneur",
            name="entrepreneurship_name",
            field=models.CharField(
                max_length=100, verbose_name="Nombre del emprendimiento"
            ),
        ),
        migrations.AlterField(
            model_name="entrepreneur",
            name="image_profile",
            field=models.ImageField(
                default="images/default.jpg",
                upload_to="images/entrepreneur_profile_pics",
                verbose_name="Foto de perfil del emprendimiento",
            ),
        ),
        migrations.AlterField(
            model_name="entrepreneur",
            name="phone_number",
            field=models.CharField(
                max_length=100, verbose_name="Número de teléfono del emprendimiento"
            ),
        ),
        migrations.CreateModel(
            name="EntrepreneurPhoto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="images/default.jpg",
                        upload_to="images/entrepreneur_photos",
                    ),
                ),
                (
                    "entrepreneur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="entrepreneurs.entrepreneur",
                    ),
                ),
            ],
        ),
    ]
