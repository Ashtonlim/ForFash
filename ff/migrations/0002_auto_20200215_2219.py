# Generated by Django 3.0.2 on 2020-02-15 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='ptype',
            new_name='typeName',
        ),
    ]
