# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import article.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150425_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default=datetime.datetime(2015, 4, 25, 20, 44, 11, 703686, tzinfo=utc), upload_to=article.models.get_upload_file_name),
            preserve_default=False,
        ),
    ]
