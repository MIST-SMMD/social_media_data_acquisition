# Copyright (c) 2023.
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @Project: social_media_data_acquisition
# @FileName: Config\config.py
# @Author：hz157
# @DateTime: 10/1/2023 下午11:20

import configparser
import os
from Utils.logutils import LogUtils

logger = LogUtils()

"""文件路径"""
# 日志文件路径
Logger_root_path = "logs"
# 可变配置文件路径
config_file_path = "Config/config.ini"
# 视频文件保存路径
media_path = "static/mdeia"
# # 图片文件保存路径
# images_root_path = "static/images"


def writeConfig(section: str, option: str, data: str):
    global config_file_path
    """
    可变配置写入
    :param section: 子标题
    :param option: 选项
    :param data: 数据值
    :return: 
    """
    try:
        iniConfig = configparser.ConfigParser()
        # 文件已存在
        if not os.path.exists(config_file_path):
            iniConfig.add_section(section)
            iniConfig.set(section, option, data)
            iniConfig.write(open(config_file_path, "w"))
        else:
            if section not in iniConfig.sections():
                iniConfig.add_section(section)
            iniConfig.read(config_file_path, encoding="utf-8")
            iniConfig.set(section, option, data)
            iniConfig.write(open(config_file_path, "w"))
        logger.info(f"Write temp config file (section: {section}, option: {option}, value: {data})")
    except Exception as e:
        logger.error(e)
    return None


def readConfig(section = None, option = None):
    global config_file_path
    """
    读取可变配置文件
    :param section: 子标题
    :param option: 选项
    :return: 可变配置文件值
    """
    try:
        iniConfig = configparser.ConfigParser()
        iniConfig.read(config_file_path, encoding="utf-8")
        if section is None and option is None:
            return iniConfig
        else:
            return iniConfig[section][option]
    except Exception as e:
        logger.error(e)
    return None


# from Utils import config

"""配置文件"""
# 设备标识
server_name = readConfig('server', 'server_name')

"""Mysql 数据库配置"""
Mysql_dialect = "mysql"
Mysql_driver = "pymysql"
# 数据库主机地址
Mysql_host = readConfig('mysql', 'host')
# 数据库端口
Mysql_port = int(readConfig('mysql', 'port'))
# 数据库用户名
Mysql_username = readConfig('mysql', 'username')
# 数据库密码
Mysql_password = readConfig('mysql', 'password')
# 数据库名
Mysql_database = readConfig('mysql', 'database')
Mysql_pool_size = 8  # 数据库连接池大小 默认5 设置为0表示无限制
Mysql_pool_recycle = 60 * 30  # 数据库自动断开时间
Mysql_echo = True # ORM转话SQL语句打印


"""新浪微博配置"""
Sina_OrgImage_Url = "https://wx3.sinaimg.cn/large/"
Sina_PC_URL = "https://s.weibo.com/weibo?q="
# Sina_PC_URL = "https://s.weibo.com/weibo?q=%E5%8E%A6%E9%97%A8%E4%B8%8B%E9%9B%A8&typeall=1&suball=1&timescope=custom%3A2023-01-05-0%3A2023-01-29-16&Refer=g&page=1"

Sina_PC_Header = {
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "accept": "not-source/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": readConfig('cookie', 'mobile')
}

Sina_Mobile_URL = "https://m.weibo.cn/status/"
Sina_Mobile_Header = {
    "User-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "accept": "not-source/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": readConfig('cookie', 'mobile')
}

Sina_Image_Header = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'X-Forwarded-For': 'm.weibo.cn'
}
