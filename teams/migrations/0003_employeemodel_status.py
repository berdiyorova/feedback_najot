# Generated by Django 5.1.1 on 2024-10-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_employeemodel_position_en_employeemodel_position_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
