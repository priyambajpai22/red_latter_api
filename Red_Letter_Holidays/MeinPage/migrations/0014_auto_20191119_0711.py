# Generated by Django 2.2 on 2019-11-19 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MeinPage', '0013_package_city_package_city_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_schedule',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_schedule', to='MeinPage.Package'),
        ),
    ]