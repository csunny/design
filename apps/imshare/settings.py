#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/6 
"""
from django.conf import settings

DOMAIN_NAME = "www.dazadapp.io"

# error code information
ERROR = {
    'FAIL': {'code': '20001', 'msg': 'request fail'},
    'WRONG_METHOD': {'code': '20002', 'msg': 'wrong method'},
    'FETCH_ERROR': {'code': '20003', 'msg': 'farm fetch file from oss error'},
    'DOWNLOAD_ERROR': {'code': '20004', 'msg': 'download model error'},
    'MODIFY_TIME_ERROR': {'code': '20005', 'msg': 'aliyun oss modify time error'},
    'MODEL_REVIEWED': {'code': '20006', 'msg': 'model had reviewed'},
    'PLATFORM_ERROR': {'code': '20007', 'msg': 'platform number not exists'},
    'ALIYUN_NOT_EXT': {'code': '20008', 'msg': 'item not find in oss'},

}
ERROR.update(settings.ERROR)

FILE_UPLOAD_PATH = settings.STATICFILES_DIRS[0]

NAS_TEST_NET = "https://testnet.nebulas.io/v1/user/getTransactionReceipt"

NAS_MAIN_NET = "https://mainnet.nebulas.io/v1/user/getTransactionReceipt"

