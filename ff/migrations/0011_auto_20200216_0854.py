# Generated by Django 3.0.2 on 2020-02-16 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ff', '0010_auto_20200216_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='rentPrice',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shoe',
            name='rentPrice',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='skirt',
            name='rentPrice',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
