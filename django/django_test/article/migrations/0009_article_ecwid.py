# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20150428_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ecwid',
            field=models.IntegerField(default=0),
        ),
    ]
