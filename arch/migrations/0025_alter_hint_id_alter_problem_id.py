# Generated by Django 4.0.7 on 2022-09-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("arch", "0024_remove_problem_aops_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hint",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="problem",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
