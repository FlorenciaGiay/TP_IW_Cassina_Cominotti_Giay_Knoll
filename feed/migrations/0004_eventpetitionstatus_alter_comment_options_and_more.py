# Generated by Django 4.1 on 2022-09-15 23:22

from django.db import migrations, models
import django.db.models.deletion

def populate_eventpetitionstatus(apps, schema_editor):
    names = [
        ("Pendiente", "#1E88E5"),
        ("Aprobado", "#43A047"),
        ("Rechazado", "#E53935"),
    ]
    EventPetitionStatus = apps.get_model("feed", "EventPetitionStatus")
    for name, color in names:
        obj = EventPetitionStatus(description=name, color=color)
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ("feed", "0003_comment_event_evententrepreneur_delete_post_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventPetitionStatus",
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
                ("description", models.CharField(max_length=100, unique=True)),
                ("color", models.CharField(default="#17a2b8", max_length=9)),
            ],
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="evententrepreneur",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="evententrepreneur",
            name="status",
            field=models.ForeignKey(
                default="Pendiente",
                on_delete=django.db.models.deletion.PROTECT,
                to="feed.eventpetitionstatus",
                to_field="description",
            ),
        ),
        migrations.RunPython(populate_eventpetitionstatus, migrations.RunPython.noop),
    ]
