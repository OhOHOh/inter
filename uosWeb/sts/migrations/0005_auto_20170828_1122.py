# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-28 03:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sts', '0004_testcase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcase',
            old_name='setName',
            new_name='caseName',
        ),
    ]
