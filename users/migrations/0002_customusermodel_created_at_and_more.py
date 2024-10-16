# Generated by Django 5.1.1 on 2024-10-09 00:05

import datetime
from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now, verbose_name='Created time:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated time', default='2024-10-09 12:34:56'),
        ),
    ]
