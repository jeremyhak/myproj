# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-11 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='voter',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]