# Generated by Django 3.2.5 on 2021-08-02 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0024_alter_unitgroup_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="semester",
            name="registration_open",
        ),
    ]
