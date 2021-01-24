# Generated by Django 3.1.1 on 2020-11-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20201114_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='people_per_room',
            field=models.IntegerField(blank=True, null=True, verbose_name='person per room'),
        ),
        migrations.AlterField(
            model_name='property',
            name='publish',
            field=models.BooleanField(choices=[(True, 'Publish'), (False, 'Arcive')], default=False, verbose_name='Post Status'),
        ),
    ]
