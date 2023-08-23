# Generated by Django 4.2.4 on 2023-08-23 21:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('hardware', 'Hardware Issue'), ('software', 'Software Issue'), ('phone', 'Phone Issue'), ('other', 'Account Issue')], max_length=200)),
                ('status', models.CharField(choices=[('Done', 'Done'), ('In Progress', 'In Progress'), ('Active', 'Active')], max_length=200)),
                ('ritm', models.CharField(blank=True, max_length=200, null=True)),
                ('technician', models.CharField(blank=True, max_length=200, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('queue_id', models.IntegerField(default=0)),
                ('is_done', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ('queue_id',),
            },
        ),
    ]
