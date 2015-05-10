# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0015_auto_20150509_2317'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default=b'', max_length=8),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_age',
            field=models.PositiveSmallIntegerField(default=b'0', verbose_name=__builtin__.max),
        ),
    ]
