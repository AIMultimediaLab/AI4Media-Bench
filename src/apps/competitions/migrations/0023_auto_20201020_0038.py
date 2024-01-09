# Generated by Django 2.2.13 on 2020-10-20 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0022_auto_20200930_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitioncreationtaskstatus',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='competition_creation_task_statuses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='competitioncreationtaskstatus',
            name='dataset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='competition_bundles', to='datasets.Data'),
        ),
    ]
