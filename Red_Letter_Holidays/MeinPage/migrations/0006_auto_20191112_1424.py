# Generated by Django 2.2 on 2019-11-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeinPage', '0005_hotel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='amenities',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='inclusive',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='meal_type',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='price',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='room_type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
