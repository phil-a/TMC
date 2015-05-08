# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20150508_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.FileField(default=b'../../assets/images/empty_profile.png-square', upload_to=userprofile.models.get_upload_file_name),
        ),
    ]
