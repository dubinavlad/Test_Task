# Generated by Django 3.1.4 on 2020-12-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0007_auto_20201224_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='last_match',
        ),
        migrations.AddField(
            model_name='team',
            name='last_match_time',
            field=models.IntegerField(default=0),
        ),
    ]
