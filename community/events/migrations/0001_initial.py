# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('start_datetime', models.DateTimeField(null=True)),
                ('end_datetime', models.DateTimeField(null=True)),
                ('location', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
