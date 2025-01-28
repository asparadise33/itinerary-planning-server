# Generated by Django 4.1.3 on 2025-01-25 20:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TravelMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_travel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('start_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField(auto_now=True)),
                ('number_of_travelers', models.IntegerField()),
                ('people_on_trip', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mode_of_travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itineraryapi.travelmode')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('uid', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TripLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tripLocations', to='itineraryapi.location')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locationTrips', to='itineraryapi.trip')),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itineraryapi.user'),
        ),
    ]
