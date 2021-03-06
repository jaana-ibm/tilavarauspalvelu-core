# Generated by Django 3.0.10 on 2021-02-02 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0010_allow_null_for_application_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationstatus',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('in_review', 'In review'), ('review done', 'Review done'), ('allocating', 'Allocating'), ('allocated', 'Allocated'), ('validated', 'Validated'), ('approved', 'Approved'), ('declined', 'Declined'), ('cancelled', 'Cancelled')], max_length=20, verbose_name='Status'),
        ),
    ]
