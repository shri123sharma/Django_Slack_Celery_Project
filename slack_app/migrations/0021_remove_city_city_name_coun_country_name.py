# Generated by Django 4.2 on 2023-04-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0020_rename_ci_name_city_city_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='city_name',
        ),
        migrations.AddField(
            model_name='coun',
            name='country_name',
            field=models.CharField(default='india', max_length=200),
            preserve_default=False,
        ),
    ]