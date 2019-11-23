# Generated by Django 2.2 on 2019-11-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeinPage', '0006_auto_20191112_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='amenities',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='inclusive',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='meal_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='room_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='package',
            name='End_date',
            field=models.DateField(max_length=255),
        ),
        migrations.AlterField(
            model_name='package',
            name='Start_date',
            field=models.DateField(max_length=255),
        ),
    ]