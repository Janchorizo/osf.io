# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-03-04 09:14
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons_teiclose', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationhistory',
            name='history',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name='annotationhistory',
            name='version',
            field=models.IntegerField(default=0),
        ),
    ]