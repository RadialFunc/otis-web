# Generated by Django 3.0.3 on 2020-04-28 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0036_auto_20200421_1159"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="extra_units",
            new_name="unlocked_units",
        ),
    ]
