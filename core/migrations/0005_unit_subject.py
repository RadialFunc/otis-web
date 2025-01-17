# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_auto_20170808_1751"),
    ]

    operations = [
        migrations.AddField(
            model_name="unit",
            name="subject",
            field=models.CharField(
                choices=[
                    ("A", "Algebra"),
                    ("C", "Combinatorics"),
                    ("G", "Geometry"),
                    ("N", "Number Theory"),
                    ("F", "Functional Equations"),
                    ("M", "Miscellaneous"),
                ],
                default="M",
                help_text="The subject for the unit",
                max_length=2,
            ),
            preserve_default=False,
        ),
    ]
