# Generated by Django 4.2.4 on 2023-08-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]