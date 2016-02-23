# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatewaysApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('customer_email', models.EmailField(unique=True, max_length=254)),
                ('customer_id', models.IntegerField(unique=True, max_length=254)),
                ('company', models.CharField(default=b'', max_length=100)),
                ('phone', models.CharField(default=b'', max_length=25)),
                ('fax', models.CharField(default=b'', max_length=25)),
                ('website', models.URLField(default=b'', max_length=75)),
            ],
        ),
    ]
