# Generated by Django 4.1.5 on 2023-01-13 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_inicial_date_event_initial_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='descripton',
            new_name='description',
        ),
    ]
