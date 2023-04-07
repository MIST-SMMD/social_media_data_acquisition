# Copyright (c) 2023.
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @Project: social_media_data_acquisition
# @FileName: Network\Files.py
# @Author：hz157
# @DateTime: 11/1/2023 上午5:13
import os
import requests
import urllib
import uuid

from Config import config
from Utils.logutils import LogUtils

logutils = LogUtils()


def DownloadWeiboImage(pid):
    """
    下载微博图片
    :param pid: 图片唯一标识
    :return:
    """
    try:
        IMAGE_URL = f"{config.Sina_OrgImage_Url}{pid}.jpg"
        r = requests.get(IMAGE_URL, headers=config.Sina_Image_Header)
        # print(r.status_code)
        # 生成uuid
        uuidCode = uuid.uuid1()
        # 写入本地
        path = f'{config.images_root_path}/{uuidCode}.jpg'
        with open(path, 'wb') as f:
            f.write(r.content)
        if os.path.exists(path):
            return [os.path.getsize(path), str(uuidCode) + '.jpg']
        else:
            return None
    except Exception as e:
        logutils.error(e)
    return None


def DownloadWeiboVideo(url):
    """
    下载微博视频
    :param url: 视频路径
    :return:
    """
    try:
        uuidCode = uuid.uuid1()
        path = f'{config.video_root_path}/{uuidCode}.mp4'
        urllib.request.urlretrieve(url, path)
        if os.path.exists(path):
            return [os.path.getsize(path), str(uuidCode) + '.mp4']
        else:
            return None
    except Exception as e:
        logutils.error(e)
    return None
