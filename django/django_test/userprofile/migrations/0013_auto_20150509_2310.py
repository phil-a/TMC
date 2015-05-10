# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_userprofile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.PositiveSmallIntegerField(default=b'0', verbose_name=9),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_age',
            field=models.PositiveSmallIntegerField(default=b'0', verbose_name=3),
        ),
    ]
