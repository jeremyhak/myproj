# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-05 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='delivery_date',
        ),
    ]