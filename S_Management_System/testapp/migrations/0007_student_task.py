# Generated by Django 3.1 on 2021-11-26 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20211124_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stask', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
