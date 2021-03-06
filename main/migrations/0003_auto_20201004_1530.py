# Generated by Django 3.1.1 on 2020-10-04 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_property_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='phone',
            new_name='contact_person',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='userid',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='property',
            name='email',
        ),
        migrations.RemoveField(
            model_name='property',
            name='property_category',
        ),
        migrations.AddField(
            model_name='property',
            name='ad_for',
            field=models.CharField(blank=True, choices=[('rent', 'Rent'), ('sale', 'Sale'), ('rtb', 'Rent for Boys'), ('rtg', 'Rent for Girls')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='advance_payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='bathroom',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='bedroom',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='empty_set',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='kitchen',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='living_room',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='parking_space',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_size',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_types',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property_types', to='main.propertytype'),
        ),
        migrations.AlterField(
            model_name='property',
            name='adress',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='propertycategory',
            name='property_types',
            field=models.ManyToManyField(blank=True, related_name='property_catagory_types', to='main.PropertyType'),
        ),
        migrations.CreateModel(
            name='Utilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('ptype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utilities', to='main.propertytype')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('ptype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_type', to='main.propertytype')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='feature_types',
            field=models.ManyToManyField(related_name='property_features', to='main.FeatureType'),
        ),
        migrations.AddField(
            model_name='property',
            name='utility_bill',
            field=models.ManyToManyField(related_name='utility_bill', to='main.Utilities'),
        ),
    ]
