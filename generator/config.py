# -*- coding: UTF-8 -*-
from flask import jsonify
import yaml
import os
import json

def load(file):
    f = open(file, 'r', encoding = 'utf-8')
    ystr = f.read()
    f.close()
    ymllist = yaml.load(ystr, Loader = yaml.SafeLoader)
    return ymllist

def read(key):
    return data[key]

data = load('config.yml')
