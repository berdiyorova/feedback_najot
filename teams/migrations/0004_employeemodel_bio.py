# Generated by Django 5.1.1 on 2024-10-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_employeemodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
