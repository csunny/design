#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/6 
"""
import os
import logging
import json
import copy
import requests
from django.shortcuts import render, HttpResponse
from imshare import settings
from django.views.decorators.csrf import csrf_exempt
from imshare.models import ImageModel
from imshare.forms import ImageModelForm
from imshare.utils import save_thumbnail

django_log = logging.getLogger("django")


def list(request):
    SITE_NAME = '迪扎网'
    images = ImageModel.objects.all()

    IMAGE_URL = "img/blockchain.jpg"
    SITE_URL = os.path.join('http://', settings.DOMAIN_NAME, 'imshare/images')
    return render(request, 'upload.html', locals())


@csrf_exempt
def update(request):
    rsp_data = copy.copy(settings.ERROR["SUCC"])

    tp = request.POST.get('type')
    if tp == 'txhash':
        name = request.POST.get('name')
        tx_hash = request.POST.get('txhash')

        ImageModel.objects.filter(name=name.strip()).update(
            tx_hash=tx_hash.strip()
        )
    elif tp == 'like':
        name = request.POST.get('name', None)
        image = ImageModel.objects.get(name=name.strip())
        image.love_count += 1
        image.save()

    image_info = ImageModel.objects.get(name=name.strip())
    rsp_data['love_count'] = image_info.love_count
    return HttpResponse(json.dumps(rsp_data), content_type="application/json")


def detail(request):
    image_name = request.GET.get('image_name')
    SITE_URL = os.path.join('http://', settings.DOMAIN_NAME, 'imshare/images')
    image_info = ImageModel.objects.get(image_name=image_name)
    return render(request, 'detail.html', locals())


@csrf_exempt
def upload(request):
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    im_info = ImageModelForm(request.POST, request.FILES)
    if im_info.is_valid():
        name = im_info.cleaned_data['name']
        image = im_info.cleaned_data['file']
        image_name = im_info.cleaned_data['image_name']
        image_model = ImageModel()
        image_model.name = name
        image_model.image_name = image_name
        image_model.image = image

        image_model.save()
        save_thumbnail(image_name, str(image))
    return HttpResponse(json.dumps(rsp_data), content_type="application/json")


@csrf_exempt
def query(request):
    """
    根据交易hash 查询作者
    :param request:
    :return:
    """
    rsp_data = copy.copy(settings.ERROR["SUCC"])
    name = request.POST.get('name')

    image = ImageModel.objects.get(name=name.strip())

    res = requests.post(url=settings.NAS_MAIN_NET, data=json.dumps({
        "hash": image.tx_hash
    }))

    rsp_data['tx_hash'] = image.tx_hash
    rsp_data['image_name'] = image.image_name
    rsp_data['image'] = str(image.image)
    rsp_data['tx_info'] = res.json()

    print(rsp_data)
    return HttpResponse(json.dumps(rsp_data), content_type="application/json")