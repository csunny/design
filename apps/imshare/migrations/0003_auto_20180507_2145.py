# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-07 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imshare', '0002_auto_20180507_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='love_count',
            field=models.IntegerField(default=0, verbose_name='点赞次数'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='tx_hash',
            field=models.CharField(default='', max_length=256, verbose_name='交易hash'),
        ),
    ]
