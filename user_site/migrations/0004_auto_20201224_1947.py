# Generated by Django 3.1.4 on 2020-12-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0003_auto_20201224_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ManyToManyField(to='user_site.Image'),
        ),
    ]
