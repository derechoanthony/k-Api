from module.controller.headerque import process_header
from flask import Flask, request, jsonify
import requests
from ver import *
app = Flask(__name__)
@app.route('/api/{ver}/search/single/user/access/<querystring>'.format(ver=ver), methods=['GET'])
def singleuserque(querystring):
    res = process_header('_singleUserSearch',querystring)
    return res
@app.route('/api/{ver}/user/list'.format(ver=ver), methods=['GET'])
def userlist():
    res = process_header('_usrlist')
    return res


if (__name__ == "__main__"):
    app.debug = True
    app.run(port = 3020)