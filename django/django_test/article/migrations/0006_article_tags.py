# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_thumbnail3'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.TextField(default=b''),
        ),
    ]
