# Generated by Django 2.2 on 2019-11-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeinPage', '0002_auto_20191115_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.CharField(default='delhi', max_length=200),
            preserve_default=False,
        ),
    ]
