# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_organization_org_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='org_tag',
            field=models.ForeignKey(to='tags.Tag'),
            preserve_default=True,
        ),
    ]
