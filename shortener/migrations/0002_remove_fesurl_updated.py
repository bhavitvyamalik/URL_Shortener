# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-05 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fesurl',
            name='updated',
        ),
    ]
