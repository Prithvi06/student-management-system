# Generated by Django 3.1 on 2021-11-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20211123_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers_class',
            name='End_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teachers_class',
            name='Start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
