# Generated by Django 4.0.8 on 2022-12-04 02:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0019_worker_twitch_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="worker",
            name="google_username",
        ),
        migrations.AddField(
            model_name="worker",
            name="gmail_address",
            field=models.CharField(
                blank=True,
                help_text="Should be of the form username@gmail.com.",
                max_length=128,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[-a-zA-Z0-9_'.]+@gmail\\.com$"
                    )
                ],
            ),
        ),
    ]
