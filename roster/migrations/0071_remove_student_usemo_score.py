# Generated by Django 3.2.6 on 2021-08-29 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0070_auto_20210820_1259"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="usemo_score",
        ),
    ]
