# Generated by Django 3.1.1 on 2021-03-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_messages_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='companyName',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='fb_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobDescription',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='web_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='yt_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
