# Generated by Django 4.1.5 on 2023-01-13 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_event_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='inicial_date',
            new_name='initial_date',
        ),
    ]
