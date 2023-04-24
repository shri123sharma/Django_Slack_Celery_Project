# Generated by Django 4.2 on 2023-04-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0024_rename_country_name_coun_coun_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coun',
            new_name='Country',
        ),
        migrations.RemoveField(
            model_name='city',
            name='city_name',
        ),
        migrations.AddField(
            model_name='state',
            name='state_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]