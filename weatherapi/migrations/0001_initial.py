# Generated by Django 2.1.5 on 2019-03-21 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherAPI',
            fields=[
                ('DATE', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('TMAX', models.FloatField()),
                ('TMIN', models.FloatField()),
            ],
        ),
    ]
