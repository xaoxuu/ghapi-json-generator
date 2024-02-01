# -*- coding: utf-8 -*-
import config
import requests
import json
import os
from urllib.parse import urlparse


GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

print('> rate_limit: \n', requests.get('https://api.github.com/rate_limit', headers=headers).content.decode())
print('> start')

def save_json(path, content):
    root = 'v2'
    dir = root + path + '/'
    file = dir + 'data.json'
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
        req = requests.get(link, headers=headers)
        path = url.path
        if url.query:
            path = path + '?' + url.query
        save_json(path, json.loads(req.content.decode()))

except Exception as e:
    print('> exception: ', e)

print('\n> rate_limit: \n', requests.get('https://api.github.com/rate_limit', headers=headers).content.decode())
print('> end')
