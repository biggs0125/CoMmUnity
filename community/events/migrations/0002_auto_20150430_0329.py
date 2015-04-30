# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('users', '0001_initial'),
        ('events', '0001_initial'),
        ('organizations', '0002_organization_admins'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(to='users.OurUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='hosts',
            field=models.ManyToManyField(to='organizations.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
            preserve_default=True,
        ),
    ]
