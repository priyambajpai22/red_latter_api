# Generated by Django 2.2 on 2019-11-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeinPage', '0003_hotel_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='image',
            field=models.ImageField(default='rahul.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]
