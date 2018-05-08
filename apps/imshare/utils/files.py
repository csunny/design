#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/7 
"""

import os
# from wand.image import Image
from imshare import settings
from PIL import Image


def resize_image(fpath, target, width, height):
    """

    :param fpath:
    :param target:
    :param width:
    :param height:
    :return:
    """
    """ 修改图片大小并保存 """

    with Image.open(fp=fpath) as img:

        img.thumbnail((width, height), Image.ANTIALIAS)

        img.save(target, "JPEG")

        # with Image(filename=fpath) as img:
        #     modify = min(size / img.size[0], size / img.size[1])
        #     if modify > 1:
        #         return
        #     width, height = [modify * img_size for img_size in img.size]
        #     img.resize(int(width), int(height))
        #     if target.endswith('bmp'):
        #         bmp3 = ''.join([target[:-3], 'bmp3'])
        #         img.save(filename=bmp3)
        #         os.system('mv %s %s' % (bmp3, target))
        #     else:
        #         img.save(filename=target)


def save_thumbnail(image_name, name):
    """
    保存
    :return:
    """
    path = os.path.join(settings.FILE_UPLOAD_PATH, 'upload')
    small_path = os.path.join(path, 'small', image_name)
    middle_path = os.path.join(path, 'middle', image_name)

    source_name = os.path.join(path, name)
    resize_image(source_name, small_path, 800, 600)
    resize_image(source_name, middle_path, 1960, 1400)
