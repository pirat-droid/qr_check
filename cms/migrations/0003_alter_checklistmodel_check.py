# Generated by Django 3.2.9 on 2021-11-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_tasksmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistmodel',
            name='check',
            field=models.BooleanField(default=None, verbose_name='Проверка'),
        ),
    ]
