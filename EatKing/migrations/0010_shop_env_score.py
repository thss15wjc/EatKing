# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EatKing', '0009_remove_shop_env_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='env_score',
            field=models.FloatField(default=None),
        ),
    ]
