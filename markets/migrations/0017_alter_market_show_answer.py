# Generated by Django 3.2.9 on 2022-01-23 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("markets", "0016_market_show_answer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="market",
            name="show_answer",
            field=models.BooleanField(default=True),
        ),
    ]
