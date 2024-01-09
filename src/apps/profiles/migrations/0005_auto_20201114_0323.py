# Generated by Django 2.2.13 on 2020-11-14 03:23

from django.db import migrations, models
import utils.data


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_user_is_bot'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='biography',
            field=models.CharField(blank=True, max_length=4096, null=True, unique=False),
        ),
        migrations.AddField(
            model_name='user',
            name='display_name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=False),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=False),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True, unique=False),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=250, null=True, unique=False),
        ),
        migrations.AddField(
            model_name='user',
            name='personal_url',
            field=models.URLField(blank=True, null=True, unique=False),
        ),
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, unique=False),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_url',
            field=models.URLField(blank=True, null=True, unique=False),
        ),
        migrations.AddField(
            model_name='user',
            name='github_url',
            field=models.URLField(blank=True, null=True, unique=False),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=utils.data.PathWrapper('profile_photos')),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]