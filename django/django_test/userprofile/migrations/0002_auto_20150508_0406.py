# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='favourite_hamster_name',
            new_name='display_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='likes_cheese',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.FileField(default=b'assets/images/empty_profile.png-square', upload_to=userprofile.models.get_upload_file_name),
        ),
    ]
