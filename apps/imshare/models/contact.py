#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/7 
"""

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=128, default="", verbose_name="姓名")
    email = models.EmailField(max_length=64, default="", verbose_name="邮箱")
    title = models.CharField(max_length=128, default="", verbose_name="标题")
    content = models.TextField(verbose_name="内容", null=True)

    def __str__(self):
        return self.name

    class Meta:
        pass

