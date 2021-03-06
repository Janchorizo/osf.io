# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-17 20:11
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.core.management.sql import emit_post_migrate_signal


def add_banner_perms_to_groups(*args, **kwargs):
    # this is to make sure that the permissions created in an earlier migration exist!
    emit_post_migrate_signal(2, False, 'default')

    view_permission = Permission.objects.get(codename='view_scheduledbanner')
    edit_permission = Permission.objects.get(codename='change_scheduledbanner')
    delete_permission = Permission.objects.get(codename='delete_scheduledbanner')

    osf_admin = Group.objects.get(name='osf_admin')
    read_only = Group.objects.get(name='read_only')

    osf_admin.permissions.add(view_permission, edit_permission, delete_permission)
    osf_admin.save()

    read_only.permissions.add(view_permission)
    read_only.save()


def remove_banner_perms_from_groups(*args, **kwargs):
    view_permission = Permission.objects.get(codename='view_scheduledbanner')
    edit_permission = Permission.objects.get(codename='change_scheduledbanner')
    delete_permission = Permission.objects.get(codename='delete_scheduledbanner')

    osf_admin = Group.objects.get(name='osf_admin')
    read_only = Group.objects.get(name='read_only')

    osf_admin.permissions.remove(view_permission, edit_permission, delete_permission)
    osf_admin.save()

    read_only.permissions.remove(view_permission)
    read_only.save()


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0077_bannerimage_scheduledbanner'),
    ]

    operations = [
        migrations.RunPython(add_banner_perms_to_groups, remove_banner_perms_from_groups),
    ]
