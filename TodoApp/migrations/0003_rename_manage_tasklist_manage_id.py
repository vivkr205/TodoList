# Generated by Django 5.1.3 on 2025-01-13 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0002_tasklist_manage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasklist',
            old_name='manage',
            new_name='manage_id',
        ),
    ]
