# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-06 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_deliver_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='deliver_on',
            field=models.DateField(default=0, null=True),
        ),
    ]