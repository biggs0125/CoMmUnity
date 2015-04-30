# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='admins',
            field=models.ManyToManyField(to='users.OurUser'),
            preserve_default=True,
        ),
    ]
