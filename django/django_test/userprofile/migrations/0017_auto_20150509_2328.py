# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0016_auto_20150509_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_age',
            field=models.CharField(default=b'', max_length=3),
        ),
    ]
