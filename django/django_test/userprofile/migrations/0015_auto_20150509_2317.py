# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0014_auto_20150509_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_age',
            field=models.CharField(default=b'', max_length=3),
        ),
    ]
