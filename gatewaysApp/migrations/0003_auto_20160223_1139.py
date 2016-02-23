# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatewaysApp', '0002_customerdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='customer_email',
            field=models.EmailField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='customer_id',
            field=models.IntegerField(unique=True),
        ),
    ]
