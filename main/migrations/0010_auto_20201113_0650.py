# Generated by Django 3.1.1 on 2020-11-13 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20201005_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.CharField(default=None, max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='property_types',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property_types', to='main.propertytype'),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(default='aj:', max_length=1000),
            preserve_default=False,
        ),
    ]
