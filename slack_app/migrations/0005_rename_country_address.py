# Generated by Django 4.2 on 2023-04-05 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0004_country'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='Address',
        ),
    ]