# -*- coding: utf-8 -*-
import config
import requests
import json
import os
from urllib.parse import urlparse

print('> rate_limit: \n', requests.get('https://api.github.com/rate_limit').content.decode())
print('> start')

def save_json(path, content):
    root = 'v2/'
    dir = root + path + '/'
    file = dir + 'data.json'
    print('> file path:', file)
    # 创建路径
    isExists = os.path.exists(dir)
    if not isExists:
        os.makedirs(dir)
    # 写入文件
    with open(file, 'w', encoding = 'utf-8') as file_obj:
        json.dump(content, file_obj, ensure_ascii = False, indent = 2)

try:
    print('> links: ', config.read('links'))
    for link in config.read('links'):
        print('> get: ', link)
        url = urlparse(link)
        print('> path: ', url.path)
        req = requests.get(link)
        save_json(url.path, json.loads(req.content.decode()))

except Exception as e:
    print('> exception: ', e)

print('> rate_limit: \n', requests.get('https://api.github.com/rate_limit').content.decode())
print('> end')
