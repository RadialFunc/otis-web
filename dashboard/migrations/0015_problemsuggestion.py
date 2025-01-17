# Generated by Django 3.0.7 on 2021-01-30 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_auto_20200908_1307"),
        ("roster", "0049_auto_20210111_1623"),
        ("dashboard", "0014_semesterdownloadfile"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProblemSuggestion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "weight",
                    models.PositiveSmallIntegerField(
                        blank=True, choices=[(2, 2), (3, 3), (5, 5), (9, 9)], null=True
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        help_text="Source of the problem, e.g. `Shortlist 2018 A7`.",
                        max_length=60,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="A one-line summary of problem, e.g. `Inequality with cube roots`.",
                        max_length=100,
                    ),
                ),
                (
                    "statement",
                    models.TextField(help_text="Statement of the problem, in LaTeX."),
                ),
                (
                    "solution",
                    models.TextField(help_text="Solution to the problem, in LaTeX."),
                ),
                (
                    "comments",
                    models.TextField(blank=True, help_text="Any extra comments."),
                ),
                (
                    "reviewed",
                    models.BooleanField(
                        default=False, help_text="Whether staff has processed this."
                    ),
                ),
                (
                    "review_notes",
                    models.TextField(blank=True, help_text="Staff notes on reviewing."),
                ),
                (
                    "student",
                    models.ForeignKey(
                        help_text="Student who suggested the problem.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="roster.Student",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        help_text="The unit to suggest the problem for.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.Unit",
                    ),
                ),
            ],
        ),
    ]
