# Generated by Django 3.0.10 on 2021-01-21 10:45

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0007_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326, verbose_name='Coordinates'),
        ),
        migrations.AddField(
            model_name='location',
            name='unit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='spaces.Unit', verbose_name='Unit'),
        ),
    ]
