# Generated by Django 2.2 on 2019-11-16 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MeinPage', '0002_auto_20191116_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='package',
            name='Cities',
        ),
        migrations.CreateModel(
            name='Package_city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_data', models.ImageField(upload_to='')),
                ('hotel_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_city', to='MeinPage.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_data', models.CharField(max_length=100)),
                ('city_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_city', to='MeinPage.Hotel')),
            ],
        ),
    ]