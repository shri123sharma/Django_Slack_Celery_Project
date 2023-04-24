# Generated by Django 4.2 on 2023-04-11 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0011_remove_city_city_capital_company_comp_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='enter actor first_name', max_length=255)),
                ('last_name', models.CharField(help_text='enter actor last_name', max_length=255)),
                ('last_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category_last_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Please enter your first name', max_length=255)),
                ('last_name', models.CharField(help_text='Please enter your last name', max_length=255)),
                ('email', models.EmailField(help_text='Please enter your email address', max_length=255, unique=True)),
                ('active_bool', models.BooleanField(default=0)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('last_update', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('release_date', models.DateField(auto_now_add=True)),
                ('rental_duration', models.SmallIntegerField(default=0.0)),
                ('length', models.SmallIntegerField(default=0)),
                ('rental_rate', models.DecimalField(decimal_places=3, default=0.0, max_digits=5)),
                ('rating', models.IntegerField(default=0)),
                ('film_last_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=255)),
                ('language_last_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_name',
            new_name='address_1',
        ),
        migrations.RemoveField(
            model_name='address',
            name='pin_code',
        ),
        migrations.RemoveField(
            model_name='city',
            name='city_pin_code',
        ),
        migrations.RemoveField(
            model_name='country',
            name='country_capital',
        ),
        migrations.RemoveField(
            model_name='country',
            name='country_pin_code',
        ),
        migrations.AddField(
            model_name='address',
            name='address_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_address', to='slack_app.city'),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='address',
            name='phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='postal_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_city', to='slack_app.country'),
        ),
        migrations.AddField(
            model_name='city',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='country',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('last_update', models.DateField(auto_now=True)),
                ('staff_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_address', to='slack_app.address')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField(auto_created=True)),
                ('return_date', models.DateField()),
                ('last_update', models.DateField(auto_now=True)),
                ('customer_rental', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='slack_app.customer')),
                ('rental_film', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='film_rental', to='slack_app.film')),
                ('rental_staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rental_staff', to='slack_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField(default=0)),
                ('payment_date', models.DateField(auto_now=True)),
                ('customer_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_payment', to='slack_app.customer')),
                ('rental', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rental_payment', to='slack_app.rental')),
                ('staff_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_payment', to='slack_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='FilmCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_category_last_update', models.DateField(auto_now=True)),
                ('category', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='slack_app.category')),
                ('film', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='slack_app.film')),
            ],
        ),
        migrations.CreateModel(
            name='FilmActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_last_update', models.DateField(auto_now=True)),
                ('actor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='slack_app.actor')),
                ('actor_film', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='slack_app.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='film_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='language_film', to='slack_app.language'),
        ),
        migrations.AddField(
            model_name='customer',
            name='address_customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_address', to='slack_app.address'),
        ),
    ]