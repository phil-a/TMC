# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import article.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_thumbnail2'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail3',
            field=models.FileField(default=0, upload_to=article.models.get_upload_file_name),
        ),
    ]
