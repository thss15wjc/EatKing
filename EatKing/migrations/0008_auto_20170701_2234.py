# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EatKing', '0007_auto_20170701_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='env',
            new_name='env_score',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='serv',
            new_name='serv_score',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='taste',
            new_name='taste_score',
        ),
    ]