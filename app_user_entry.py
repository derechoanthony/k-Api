#!flask/bin/python
from module.controller.headerque import process_header
from flask import Flask, request, jsonify
import requests
from ver import *

app = Flask(__name__)

@app.route('/api/{ver}/user/entry'.format(ver=ver), methods=['POST'])
def create_user():
    res = process_header('_userEntryData')
    return res
@app.route('/api/{ver}/new/user/access'.format(ver=ver), methods=['POST'])
def create_user_access():
    res = process_header('_userNewAccess')
    return res


if (__name__ == "__main__"):
    app.debug = True
    app.run(port = 3010)