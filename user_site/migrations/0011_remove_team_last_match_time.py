# Generated by Django 3.1.4 on 2020-12-29 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0010_auto_20201225_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='last_match_time',
        ),
    ]
