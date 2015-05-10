# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0017_auto_20150509_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default=b'CA', max_length=2, choices=[(b'CA', b'Canada'), (b'US', b'United States')]),
        ),
    ]
