# Generated by Django 4.2.7 on 2023-11-08 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='gas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('weight', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.consumer')),
            ],
        ),
        migrations.CreateModel(
            name='electricityUnits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('units', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.consumer')),
            ],
        ),
        migrations.CreateModel(
            name='dailyHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('totalAc', models.FloatField()),
                ('totalElectricity', models.FloatField()),
                ('totalGas', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.consumer')),
            ],
        ),
        migrations.CreateModel(
            name='airConditionerUnits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.FloatField()),
                ('ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.airconditioner')),
            ],
        ),
    ]
