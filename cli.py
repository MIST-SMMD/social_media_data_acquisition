# Copyright (c) 2023.
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @Project: social_media_data_acquisition
# @FileName: cli.py
# @Author：hz157
# @DateTime: 10/1/2023 下午9:55
import os
import platform
import time

import Config.config
import app

os_name = platform.system()
clear_command = 'cls' if os_name == 'Windows' else 'clear'

iniContent = {
    'mysql': ['host', 'port', 'username', 'password', 'database'],
    'cookie': ['pc', 'mobile']
}


def menu():
    os.system(clear_command)
    print("""
    git: https://github.com/MIST-SMMD
        1. Edit Param
        2. Start Get Weibo Data
        q. Exit
    """)
    keyBoard = input()
    if keyBoard == '1':
        os.system(clear_command)
        displayParam()
        editParam()
    elif keyBoard == '2':
        os.system(clear_command)
        keyword = input("Please Input Spider Keyword: ")
        while True:
            isDatabase = input('Whether to write to the database(Y/N): ')
            if isDatabase.lower() == 'n':
                app.main(keyword, 'print')
                break
            elif isDatabase.lower() == 'y':
                app.main(keyword, 'datebase')
                break
            else:
                print('Input error')

    elif keyBoard == 'q':
        exit(0)


def editParam():
    print("""
    1. Database
    2. Cookie
    """)
    keyBoard = input()
    if keyBoard == '1':
        for item in iniContent['mysql']:
            data = input(f"Please Input database - {item}: ")
            Config.config.writeConfig('mysql', item, data)
            time.sleep(0.5)
    else:
        for item in iniContent['cookie']:
            data = input(f"Please Input {item} - cookie: ")
            Config.config.writeConfig('cookie', item, data)
            time.sleep(0.5)
    menu()


def displayParam():
    params = Config.config.readConfig()
    for section in params:
        print(f"[{section}]")
        for option in params[section]:
            print(f"    -{option}: {params[section][option]}")

if __name__ == '__main__':
    menu()
