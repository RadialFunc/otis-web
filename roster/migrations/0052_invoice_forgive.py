# Generated by Django 3.1.8 on 2021-05-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0051_auto_20210410_1117"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="forgive",
            field=models.BooleanField(
                default=False,
                help_text="When switched on, won't hard-lock delinquents.",
            ),
        ),
    ]
