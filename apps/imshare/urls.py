#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/6 
"""

from django.conf.urls import url
from imshare.views import image, contact

urlpatterns = [
    url(r'^images$', image.list),
    url(r'^detail$', image.detail),
    url(r'^upload$', image.upload),
    url(r'^update$', image.update),
    url(r'^query$', image.query),

    url(r'^contact$', contact.contact),

]
