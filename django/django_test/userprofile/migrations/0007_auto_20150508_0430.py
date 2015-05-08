# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20150508_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.FileField(default=b'/Users/philip/Development/Python/TMC/django/django_test/staticfiles/assets/images/tmc.png', upload_to=userprofile.models.get_upload_file_name),
        ),
    ]
