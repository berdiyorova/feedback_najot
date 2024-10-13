# Generated by Django 5.1.1 on 2024-10-13 05:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0009_remove_commentsmodel_text_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsmodel',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='feedback.offermodel'),
        ),
        migrations.AddField(
            model_name='commentsmodel',
            name='problem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='feedback.problemmodel'),
        ),
    ]
