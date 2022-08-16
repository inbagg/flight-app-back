# Generated by Django 4.0.4 on 2022-08-15 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline_Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Airline Companies',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_Time', models.DateTimeField(null=True)),
                ('landing_Time', models.DateTimeField(null=True)),
                ('remaining_Tickets', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.TextField(blank=True, default='', null=True)),
                ('airline_Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flight_companies.airline_company')),
                ('destination_Country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flight_destanation', to='flight_companies.country')),
                ('origin_Country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flight_origin', to='flight_companies.country')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('flight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flight_companies.flight')),
            ],
        ),
        migrations.AddField(
            model_name='airline_company',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flight_companies.country'),
        ),
        migrations.AddField(
            model_name='airline_company',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]