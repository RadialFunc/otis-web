# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-06 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0005_auto_20170806_0031"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="name",
            field=models.CharField(
                default="Nameless Student",
                help_text="The display name for this student (e.g. a nickname)",
                max_length=80,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ta",
            name="name",
            field=models.CharField(
                default="Nameless TA",
                help_text="The display name for this TA (e.g. a nickname)",
                max_length=80,
            ),
            preserve_default=False,
        ),
    ]
