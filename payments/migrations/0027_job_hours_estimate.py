# Generated by Django 4.0.8 on 2022-12-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0026_remove_job_due_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="hours_estimate",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Optional estimate for how number of hours this took. Has no effect on your payment, but useful for me to know to make sure I'm not underpaying people broadly speaking. Decimal numbers are allowed.",
                max_digits=6,
                null=True,
            ),
        ),
    ]
