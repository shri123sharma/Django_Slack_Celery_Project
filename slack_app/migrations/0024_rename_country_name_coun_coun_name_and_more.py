# Generated by Django 4.2 on 2023-04-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0023_rename_coun_name_coun_country_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coun',
            old_name='country_name',
            new_name='coun_name',
        ),
        migrations.RemoveField(
            model_name='state',
            name='state_name',
        ),
        migrations.AddField(
            model_name='city',
            name='city_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]