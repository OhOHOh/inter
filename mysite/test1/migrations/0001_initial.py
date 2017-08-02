# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-17 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAlive', models.BooleanField(default=False)),
                ('beginTime', models.DateTimeField()),
                ('nowTime', models.DateTimeField(auto_now=True, verbose_name='当前时间')),
                ('text', models.TextField()),
            ],
        ),
    ]