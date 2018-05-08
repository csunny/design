#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/7 
"""
from django.db import models


class ImageModel(models.Model):
    name = models.CharField(max_length=128, verbose_name="名称")
    image = models.FileField(upload_to="./static/upload", verbose_name="文件")
    image_name = models.CharField(max_length=128, default="", verbose_name="图片名称")
    tx_hash = models.CharField(max_length=256, default="", verbose_name="交易hash")
    love_count = models.IntegerField(default=0, verbose_name="点赞次数")

    def __str__(self):
        return self.name

    class Meta:
        pass
