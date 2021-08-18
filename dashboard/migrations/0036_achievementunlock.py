# Generated by Django 3.2.6 on 2021-08-18 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0035_remove_problemsuggestion_notified'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementUnlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='The time the achievement was granted')),
                ('achievement', models.ForeignKey(help_text='The achievement that was obtained', on_delete=django.db.models.deletion.CASCADE, to='dashboard.achievement')),
                ('user', models.ForeignKey(help_text='The user who unlocked the achievement', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
