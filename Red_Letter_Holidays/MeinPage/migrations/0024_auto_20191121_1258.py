# Generated by Django 2.2 on 2019-11-21 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MeinPage', '0023_hotel_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='package',
            name='updated',
        ),
    ]