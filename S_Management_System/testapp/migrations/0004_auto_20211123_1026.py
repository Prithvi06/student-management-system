# Generated by Django 3.1 on 2021-11-23 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20211123_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sports_game',
            old_name='Players',
            new_name='No_of_Players',
        ),
        migrations.RenameField(
            model_name='sports_game',
            old_name='Timing_in_hour',
            new_name='Playing_hours',
        ),
    ]