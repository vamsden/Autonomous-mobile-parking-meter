# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('manufacturer', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('owners', models.ForeignKey(to='cars.User')),
            ],
        ),
    ]
