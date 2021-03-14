# -*- coding: UTF-8 -*-
from flask import Flask, request, jsonify, redirect, make_response
import requests
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

def github_json(api_repo, target):
    source_url = 'https://raw.githubusercontent.com/' + api_repo + '/output/v1/' + target
    print('> get: ', source_url)
    req = requests.get(source_url)
    content = []
    if req.content:
        content = json.loads(req.content.decode())
    resp = make_response(jsonify(
        code = 0,
        source_url = source_url,
        content = content
    ))
    resp.status = '200'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET'
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp


@app.route('/v1', methods=['GET'])
def start_list():
    return jsonify(
        contributors = "https://github-api-xaoxuu.vercel.app/v1/contributors?api={owner/repo}&repo={owner/repo}",
        releases = "https://github-api-xaoxuu.vercel.app/v1/releases?api={owner/repo}&repo={owner/repo}"
    )

@app.route('/v1/<type>', methods=['GET'])
def start_main(type):
    api_repo = request.args.get("api") or 'xaoxuu/github-api'
    repo = request.args.get("repo") or 'xaoxuu/github-api'
    target = repo + '/' + type + '.json'
    return github_json(api_repo + '/main', target)
