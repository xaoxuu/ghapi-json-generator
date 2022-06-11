# -*- coding: utf-8 -*-
import config
import requests
import yaml
import json
import os

baselink = {
    "users": "https://api.github.com/users/",
    "repos": "https://api.github.com/repos/"
}

def save_json(repo, type, content):
    root = 'v1/'
    dir = root + repo + '/'
    file = dir + type + '.json'
    # 创建路径
    isExists = os.path.exists(dir)
    if not isExists:
        os.makedirs(dir)
    # 写入文件
    with open(file, 'w', encoding = 'utf-8') as file_obj:
        json.dump(content, file_obj, ensure_ascii = False)


print('> rate_limit: \n', requests.get('https://api.github.com/rate_limit').content.decode())
print('> start')

try:
    # users
    print('> users: ', config.read('users'))
    for item in config.read('users'):
        api_url = baselink['users'] + item
        print('> get: ', api_url)
        req = requests.get(api_url)
        save_json(item, 'users', json.loads(req.content.decode()))
    # repos
    type_list = ['contributors', 'releases', 'issues', 'stargazers']
    for type in type_list:
        print('> ' + type + ': ', config.read(type))
        for item in config.read(type):
            api_url = baselink['repos'] + item + '/' + type
            print('> get: ', api_url)
            req = requests.get(api_url)
            save_json(item, type, json.loads(req.content.decode()))
except Exception as e:
    print('> exception: ', e)

print('> rate_limit: \n', requests.get('https://api.github.com/rate_limit').content.decode())
print('> end')
