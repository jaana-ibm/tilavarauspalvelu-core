# Generated by Django 3.0.10 on 2020-12-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_application_model_refinements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationperiod',
            name='application_period_begin',
            field=models.DateTimeField(verbose_name='Application period begin'),
        ),
        migrations.AlterField(
            model_name='applicationperiod',
            name='application_period_end',
            field=models.DateTimeField(verbose_name='Application period end'),
        ),
    ]