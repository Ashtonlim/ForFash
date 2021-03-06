# Generated by Django 3.0.2 on 2020-02-15 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(default='Product Type', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Shoe Type', max_length=150, unique=True)),
                ('brand', models.CharField(default='Brandless', max_length=80, unique=True)),
                ('desc', models.TextField(max_length=400)),
                ('thumbnail1', models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/shoes')),
                ('thumbnail2', models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/shoes')),
                ('thumbnail3', models.ImageField(default='default-thumbnail-shoes.png', upload_to='thumbnails/shoes')),
                ('size', models.DecimalField(choices=[(5.0, 'US 5.0'), (5.5, 'US 5.5'), (6.0, 'US 6.0'), (6.5, 'US 6.5'), (7.0, 'US 7.0'), (7.5, 'US 7.5'), (8.0, 'US 8.0'), (8.5, 'US 8.5'), (9.0, 'US 9.0'), (9.5, 'US 9.5'), (10.0, 'US 10.0'), (10.5, 'US 10.5'), (11.0, 'US 11.0'), (11.5, 'US 11.5'), (12.0, 'US 12.0'), (13.0, 'US 13.0'), (14.0, 'US 14.0'), (15.0, 'US 15.0'), (16.0, 'US 16.0')], decimal_places=1, max_digits=3)),
                ('ptype', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ptype', to='ff.ProductType')),
            ],
        ),
    ]
