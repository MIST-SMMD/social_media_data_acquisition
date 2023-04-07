# Copyright (c) 2023.
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @Project: social_media_data_acquisition
# @FileName: Utils\convert.py
# @Author：hz157
# @DateTime: 11/1/2023 上午1:19

from datetime import datetime

from Utils.logutils import LogUtils

logutils = LogUtils()


def CNConvertInt(data: str):
    try:
        data = data.replace("次播放", "")
        unit = ["万", "亿"]
        default_dic = {"万": 10000, "亿": 100000000}
        current = {}
        if data[-1] in unit:
            current = default_dic[data[-1]]
        else:
            return int(data)
        data = data[0:-1]
        point = data.split(".")
        point[1] = "0." + point[1]
        for i in range(0, len(point)):
            point[i] = float(point[i])
            point[i] = point[i] * current
        result = point[0] + point[1]
        return int(result)
    except Exception as e:
        pass
        # logutils.error(e)
    return None


def UTCConvertFormat(date):
    """_summary_

    Args:
        date (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        cat = datetime.strptime(date, "%a %b %d %H:%M:%S %z %Y")
        return cat.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        pass
        # logutils.error(e)
    return None


def fileSizeConvert(size: int):
    result = ''
    try:
        if size < 1024:
            result = str(size) + "B"
        elif size > 1024:
            result = str(size / float(1024)) + "KB"
        elif size > 10240:
            result = str(size / float(1024) / float(1024)) + "MB"
        elif size > 102400:
            result = str(size / float(1024) / float(1024) / float(1024)) + "GB"
        return result
    except Exception as e:
        logutils.error(e)
    return None
