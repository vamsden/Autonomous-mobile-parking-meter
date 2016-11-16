# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=30, default='Australia'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
