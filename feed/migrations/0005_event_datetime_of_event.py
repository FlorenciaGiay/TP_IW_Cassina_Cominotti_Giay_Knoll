# Generated by Django 4.1 on 2022-09-19 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feed", "0004_eventpetitionstatus_alter_comment_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="datetime_of_event",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
