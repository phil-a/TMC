# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20150508_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(default=b'CA', max_length=2, choices=[(b'CA', b'Canada'), (b'US', b'United States')])),
            ],
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='display_name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.PositiveSmallIntegerField(default=b'0', verbose_name=__builtin__.max),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='postal_code',
            field=models.CharField(default=b'', max_length=8),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='province',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
