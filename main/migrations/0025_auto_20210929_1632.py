# Generated by Django 3.1.1 on 2021-09-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_property_varified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, max_length=11000, null=True, unique=True),
        ),
    ]
