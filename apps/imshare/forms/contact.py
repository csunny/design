#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/7 
"""

from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    title = forms.CharField()
    content = forms.Textarea()



