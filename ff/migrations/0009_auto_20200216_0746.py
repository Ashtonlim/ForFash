# Generated by Django 3.0.2 on 2020-02-15 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ff', '0008_auto_20200216_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='retailPrice',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bag',
            name='name',
            field=models.CharField(default='Bag Type', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='bag',
            name='thumbnail1',
            field=models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/bags'),
        ),
        migrations.AlterField(
            model_name='bag',
            name='thumbnail2',
            field=models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/bags'),
        ),
        migrations.AlterField(
            model_name='bag',
            name='thumbnail3',
            field=models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/bags'),
        ),
        migrations.AlterField(
            model_name='skirt',
            name='name',
            field=models.CharField(default='Skirt Type', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='skirt',
            name='thumbnail1',
            field=models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/skirt'),
        ),
        migrations.AlterField(
            model_name='skirt',
            name='thumbnail2',
            field=models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/skirt'),
        ),
        migrations.AlterField(
            model_name='skirt',
            name='thumbnail3',
            field=models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/skirt'),
        ),
    ]