# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-20 03:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_article_deliver_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='deliver_on',
        ),
    ]
