# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EatKing', '0002_auto_20170630_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='like_shop_num',
            field=models.CharField(default=None, max_length=128),
        ),
    ]
