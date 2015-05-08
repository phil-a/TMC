# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20150508_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.FileField(default=b'https://img-w.zeebox.com/images/profile/generic/Empty_Profile_06.png:square', upload_to=userprofile.models.get_upload_file_name),
        ),
    ]
