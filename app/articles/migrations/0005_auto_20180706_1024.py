# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-06 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20180706_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='deliver_on',
            field=models.DateField(null=True),
        ),
    ]