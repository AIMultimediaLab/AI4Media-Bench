# Generated by Django 2.1.2 on 2019-11-04 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('queues', '0001_initial'),
        ('competitions', '0003_auto_20190925_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='queue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='competitions', to='queues.Queue'),
        ),
    ]
