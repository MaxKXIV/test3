# Generated by Django 4.2.11 on 2024-03-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_restaurants_manager_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='rest_close',
            field=models.TimeField(default='21:00', verbose_name='%H:%M'),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='rest_open',
            field=models.TimeField(default='11:00', verbose_name='%H:%M'),
        ),
    ]