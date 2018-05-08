#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/7 
"""

from django import forms


class ImageModelForm(forms.Form):
    name = forms.CharField()
    file = forms.FileField()
    image_name = forms.CharField()


