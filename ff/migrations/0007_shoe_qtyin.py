# Generated by Django 3.0.2 on 2020-02-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ff', '0006_auto_20200215_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='qtyin',
            field=models.PositiveSmallIntegerField(default='10'),
        ),
    ]
