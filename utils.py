# -*- coding: utf-8 -*-

"""
    Created by huangming on 03/02/2018.
"""

import requests
from bs4 import BeautifulSoup
import os
import json


def fetch_page(page_url):
    try:
        r = requests.get(page_url)
        return BeautifulSoup(r.text, 'lxml')
    except Exception as e:
        print(e)
        return None


def get_data_json_file_path(key):
    return os.path.join(get_data_dir_path(), key + '.json')


def get_data_dir_path():
    # 获取当前工程目录路径
    print(os.getcwd())
    # 获取当前python文件路径
    print(__file__)
    # 获取当前python文件的f父路径
    print(os.path.dirname(__file__))

    data_dir_path = os.path.join(os.path.dirname(__file__), 'data')
    print(data_dir_path)
    return data_dir_path

def save_data_json_to_local(key, data):
    data_file_path = get_data_json_file_path(key)
    # str
    json_data = json.dumps(data, ensure_ascii=False)
    with open(data_file_path, mode='w', encoding='utf-8') as f:
        f.write(json_data)




if __name__ == '__main__':
    soup = fetch_page('http://www.yousuu.com')
    print(type(soup))
