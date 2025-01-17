# Generated by Django 3.2.8 on 2021-10-19 15:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0037_rename_last_announce_dismiss_userprofile_last_email_dismiss"),
    ]

    operations = [
        migrations.CreateModel(
            name="Market",
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
                    "start_date",
                    models.DateTimeField(
                        help_text="When the market becomes visible to players"
                    ),
                ),
                ("end_date", models.DateTimeField(help_text="When the market closes")),
                (
                    "slug",
                    models.SlugField(help_text="Slug for the market", unique=True),
                ),
                (
                    "title",
                    models.CharField(help_text="Title of the market", max_length=80),
                ),
                ("prompt", models.TextField(help_text="Full text of the question")),
                ("answer", models.FloatField(help_text="The answer to the question")),
                (
                    "semester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.semester"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Guess",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "value",
                    models.FloatField(
                        help_text="User's guess",
                        validators=[
                            django.core.validators.MinValueValidator(
                                0.01, message="Need to enter a number at least 0.01."
                            )
                        ],
                    ),
                ),
                (
                    "score",
                    models.FloatField(
                        help_text="The score for the guess, computed by the backend."
                    ),
                ),
                (
                    "public",
                    models.BooleanField(
                        help_text="If checked, will display your name next to your guess in the statistics, for bragging rights. By default, this is off and your guess is recorded anonymously."
                    ),
                ),
                (
                    "market",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="markets.market"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
