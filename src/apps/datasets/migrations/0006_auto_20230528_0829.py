# Generated by Django 2.2.17 on 2023-05-28 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0005_auto_20230527_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='submission', to='competitions.Competition'),
        ),
    ]
