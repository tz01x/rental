# Generated by Django 3.1.1 on 2020-10-01 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imguploading', '0003_auto_20201001_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='hotel_Main_Img',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='timg',
        ),
    ]
