# Generated by Django 4.2.4 on 2023-08-23 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_phone_no'),
        ('pages', '0004_alter_items_stock_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='allocated_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
