# Generated by Django 2.2.4 on 2019-10-24 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0003_auto_20191024_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='warrant',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]