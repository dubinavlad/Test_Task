# Generated by Django 3.1.4 on 2020-12-24 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_site", "0008_auto_20201224_2307"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="logo",
            field=models.CharField(max_length=255),
        ),
    ]
