# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='clothing_style',
            field=models.CharField(default=b'PROFESSIONAL', max_length=4, choices=[(b'PROFESSIONAL', b'Professional'), (b'STREET', b'Street'), (b'PREP', b'Prep')]),
        ),
    ]
