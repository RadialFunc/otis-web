# Generated by Django 3.0.3 on 2020-04-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0035_auto_20191214_2320"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="track",
            field=models.CharField(
                choices=[
                    ("A", "Weekly"),
                    ("B", "Biweekly"),
                    ("BW", "Biwk. WS"),
                    ("C", "Corr."),
                    ("CW", "Corr. WS"),
                    ("E", "Ext."),
                    ("G", "Grad"),
                    ("N", "N.A."),
                    ("P", "Phantom"),
                ],
                help_text="The track that the student is enrolled in for this semester.",
                max_length=5,
            ),
        ),
    ]
