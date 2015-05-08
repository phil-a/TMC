# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20150508_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_age',
            field=models.PositiveSmallIntegerField(default=b'0', verbose_name=__builtin__.max),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default=b'/static/assets/images/tmc.png', upload_to=userprofile.models.get_upload_file_name),
        ),
    ]
