# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0005_uploadedfile_created_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="uploadedfile",
            options={"ordering": ("-created_at",)},
        ),
    ]
