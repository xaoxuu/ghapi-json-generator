# -*- coding: utf-8 -*-
import requests
import yaml
import json
import os

def load_config():
    f = open('config.yml', 'r', encoding = 'utf-8')
    ystr = f.read()
    ymllist = yaml.load(ystr, Loader = yaml.FullLoader)
    return ymllist

def save_json(repo, type, content):
    root = 'output/v1/'
    dir = root + repo + '/'
    file = dir + type + '.json'
    # 创建路径
    isExists = os.path.exists(dir)
    if not isExists:
        os.makedirs(dir)
    # 写入文件
    with open(file, 'w', encoding = 'utf-8') as file_obj:
        json.dump(content, file_obj, ensure_ascii = False)


print('> rate_limit: \n', requests.get('https://api.github.com/rate_limit').content)
print('> start')

baselink = 'https://api.github.com/repos/'
config = load_config()
try:
    print('> contributors:', config['contributors'])
    for repo in config['contributors']:
        api = baselink + repo + '/contributors'
        print('> get: ', api)
        req = requests.get(api)
        save_json(repo, 'contributors', json.loads(req.content.decode()))
    print('> releases:', config['releases'])
    for repo in config['releases']:
        api = baselink + repo + '/releases'
        print('> get: ', api)
        req = requests.get(api)
        save_json(repo, 'releases', json.loads(req.content.decode()))
except Exception as e:
    print('> end: ', e)
print('> end')
