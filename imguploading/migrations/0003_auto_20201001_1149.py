# Generated by Django 3.1.1 on 2020-10-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imguploading', '0002_hotel_timg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseimage', models.ImageField(upload_to='images/')),
                ('timage', models.ImageField(upload_to='timage/')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='images',
            field=models.ManyToManyField(related_name='multipleImages', to='imguploading.Images'),
        ),
    ]
