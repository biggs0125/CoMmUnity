# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('organizations', '0002_organization_admins'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='org_tag',
            field=models.ForeignKey(default=None, to='tags.Tag'),
            preserve_default=True,
        ),
    ]
