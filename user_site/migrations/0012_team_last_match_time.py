# Generated by Django 3.1.4 on 2020-12-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_site", "0011_remove_team_last_match_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="last_match_time",
            field=models.DateField(default=None),
        ),
    ]
