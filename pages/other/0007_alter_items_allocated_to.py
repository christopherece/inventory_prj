# Generated by Django 4.2.4 on 2023-08-25 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_phone_no'),
        ('pages', '0006_alter_items_allocated_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='allocated_to',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='users.profile'),
            preserve_default=False,
        ),
    ]
