# Generated by Django 2.2.4 on 2019-10-24 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='warrant',
            field=models.BooleanField(default=False),
        ),
    ]
