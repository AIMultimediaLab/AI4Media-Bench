# Generated by Django 2.2.17 on 2023-08-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0034_auto_20230727_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='report',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='reward',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
