# Generated by Django 4.0.8 on 2022-12-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0021_jobfolder_max_pending_jobfolder_max_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="progress",
            field=models.CharField(
                choices=[
                    ("NEW", "In progress"),
                    ("REV", "Revisions requested"),
                    ("SUB", "Submitted"),
                    ("VFD", "Completed"),
                ],
                default="NEW",
                help_text="The current status of the job",
                max_length=3,
            ),
        ),
    ]
