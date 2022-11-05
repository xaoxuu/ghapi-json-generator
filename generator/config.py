# -*- coding: UTF-8 -*-
import yaml

def load(file):
    f = open(file, 'r', encoding = 'utf-8')
    ystr = f.read()
    f.close()
    ymllist = yaml.load(ystr, Loader = yaml.SafeLoader)
    return ymllist

def read(key):
    return data[key]

data = load('config.yml')
