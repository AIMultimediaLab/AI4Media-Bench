# Generated by Django 2.2.13 on 2020-10-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0004_remove_leaderboard_competition'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='submission_rule',
            field=models.TextField(blank=True, choices=[('Add', 'Only allow adding one submission'), ('Add_And_Delete', 'Allow users to add a single submission and remove that submission'), ('Add_By_Review', 'Only allow adding one submission that is approved by review'), ('Force_Last', 'Force only the last submission'), ('Force_Latest_Multiple', 'Force latest submission to be added to leaderboard (multiple)'), ('Force_Latest_Multiple', 'Force only the best submission to the leaderboard')], null=True),
        ),
    ]
