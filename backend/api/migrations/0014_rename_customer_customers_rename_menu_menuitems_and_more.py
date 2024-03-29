# Generated by Django 4.2.11 on 2024-03-07 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_order_order_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Customers',
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItems',
        ),
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='menu',
            new_name='menuItems',
        ),
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='Restaurants',
        ),
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('manager_id', models.AutoField(primary_key=True, serialize=False)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager_restaurant', to='api.restaurants')),
            ],
        ),
    ]
