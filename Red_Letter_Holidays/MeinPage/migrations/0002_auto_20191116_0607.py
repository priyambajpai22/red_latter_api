# Generated by Django 2.2 on 2019-11-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeinPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='hotel',
        ),
        migrations.AddField(
            model_name='package',
            name='hotel',
            field=models.ManyToManyField(related_name='hotel', to='MeinPage.Hotel'),
        ),
    ]