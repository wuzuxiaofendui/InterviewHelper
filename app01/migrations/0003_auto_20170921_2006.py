# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20170921_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo2company',
            name='company',
        ),
        migrations.RemoveField(
            model_name='userinfo2company',
            name='userinfo',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='iviewed_companys',
            new_name='companys',
        ),
        migrations.DeleteModel(
            name='UserInfo2Company',
        ),
    ]
