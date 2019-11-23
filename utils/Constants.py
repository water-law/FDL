#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""此模块是应用程序用到的一些常量，
为了解耦单独放在一个文件
"""
import os
import json
import locale
import mimetypes

mimetypes.common_types.update(mimetypes.types_map)
known_types = mimetypes.common_types
unicode = str


def _get_file_typelist(filetype):
    result = []
    for key, value in known_types.items():
        if value.startswith(filetype):
            result.append(unicode(key))
    return result


# the paths
LOCAL_ENCODING = locale.getpreferredencoding()
current_path = os.path.abspath(__file__)  # current path of the application
folder_path = os.path.dirname(os.path.dirname(current_path))
DATA_DIR = os.path.join(folder_path, "data")  # 数据库文件存放的路径
CONFIG_PATH = os.path.join(DATA_DIR, "config")


def getConfValue(k):
    data = json.load(open("conf.json", "rb"))
    conf = data.get(k)
    if conf is None:
        return None
    try:
        value = conf["value"]
    except KeyError:
        value = conf["default"]
    return value if value != "" else None


def setConfValue(k, v):
    data = json.load(open("conf.json", "rb"))
    conf = data.get(k)
    conf["value"] = v
    json.dump(data, open("conf.json", "w"))

# the types

MUSIC_TYPE = [".mp3", ".wav", ".aac"] + (_get_file_typelist("audio"))  # 文件类型识别，暂时只是用后缀名
MOVIE_TYPE = [".mp4", ".rvmb", ".swf"] + (_get_file_typelist("video"))
DOC_TYPE = [".pdf", ".doc", ".ppt", ".txt", ".php"] + (_get_file_typelist("text"))
PIC_TYPE = [".png", ".jpg", ".gif"] + (_get_file_typelist("image"))
APPLICATION_TYPE = _get_file_typelist("application")

if __name__ == '__main__':
    print("current path", current_path)
    print(_get_file_typelist("audio"))
    print(_get_file_typelist("application"))
    print("|".join(["/.*(?!\.%s$)/" % i[1:] for i in DOC_TYPE]))
