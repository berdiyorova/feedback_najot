# Generated by Django 5.1.1 on 2024-10-09 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='position_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Position of employee'),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='position_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Position of employee'),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='position_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Position of employee'),
        ),
    ]
