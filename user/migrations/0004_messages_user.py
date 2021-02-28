# Generated by Django 3.1.1 on 2021-02-13 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='message', to='auth.user'),
            preserve_default=False,
        ),
    ]