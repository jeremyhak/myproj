# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-06 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_delivery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='deliver_on',
            field=models.DateField(default=None),
        ),
    ]