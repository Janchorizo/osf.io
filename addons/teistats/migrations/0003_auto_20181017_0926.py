# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-17 09:26
from __future__ import unicode_literals

from django.db import migrations
import osf.utils.datetime_aware_jsonfield


class Migration(migrations.Migration):

    dependencies = [
        ('addons_teistats', '0002_teistatistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teistatistics',
            name='calculations',
            field=osf.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(blank=True, default={b'meta': {b'finished': False, b'maxLines': 0, b'teiFiles': 0, b'totalFiles': 0}, b'statistics': []}, encoder=osf.utils.datetime_aware_jsonfield.DateTimeAwareJSONEncoder),
        ),
    ]
