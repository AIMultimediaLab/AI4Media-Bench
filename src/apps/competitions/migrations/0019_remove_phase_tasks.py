# Generated by Django 2.2.13 on 2020-09-21 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0018_auto_20200921_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phase',
            name='tasks',
        ),
    ]
