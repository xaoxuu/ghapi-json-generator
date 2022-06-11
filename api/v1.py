# -*- coding: UTF-8 -*-
from flask import Flask, request, jsonify, redirect, make_response
import requests
import json
import yaml

app = Flask(__name__)

# read config
def load_settings(key):
    f = open('config.yml', 'r', encoding = 'utf-8')
    ystr = f.read()
    f.close()
    data = yaml.load(ystr, Loader = yaml.SafeLoader)
    return data['settings'][key]


def github_json(api_repo, target):
    source_url = 'https://raw.githubusercontent.com/' + api_repo + '/v1/' + target
    print('> get: ', source_url)
    req = requests.get(source_url)
    if req.status_code == 200:
        print('> req.content: ', req.content)
        data = json.loads(req.content.decode())
        resp = make_response(json.dumps(data, indent=2))
        resp.status = '200'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET'
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp
    else:
        resp = make_response(req.content)
        resp.status = '404'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET'
        return resp


@app.route('/v1', methods=['GET'])
def start_list():
    data = {
        "users": "https://gh-api.xaoxuu.com/v1/users?source={owner/repo}&target={owner}",
        "contributors": "https://gh-api.xaoxuu.com/v1/contributors?source={owner/repo}&target={owner/repo}",
        "releases": "https://gh-api.xaoxuu.com/v1/releases?source={owner/repo}&target={owner/repo}",
        "issues": "https://gh-api.xaoxuu.com/v1/issues?source={owner/repo}&target={owner/repo}"
    }
    resp = make_response(json.dumps(data, indent=2))
    resp.status = '200'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET'
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp

@app.route('/v1/<type>', methods=['GET'])
def start_main(type):
    source = request.args.get("source") or load_settings('source_repo')
    source += '/output'
    target = request.args.get("target")
    if target:
        target += '/' + type + '.json'
        return github_json(source, target)
    else:
        api_url = 'https://gh-api.xaoxuu.com/v1/'
        api_url += type + '?' + 'source={owner/repo}'
        api_url += '&target='
        if type == 'users':
            api_url += '{owner}'
        else:
            api_url += '{owner/repo}'
        return {type: api_url}
