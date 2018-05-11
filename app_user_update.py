from module.controller.headerque import process_header
from flask import Flask, request, jsonify
import requests
from ver import *
app = Flask(__name__)
print ver
@app.route('/api/{ver}/edit/user/account'.format(ver=ver), methods=['POST'])
def userEditfunc():
    res = process_header('_userEdit')
    return res
@app.route('/api/{ver}/remove/user/account/<q>'.format(ver=ver), methods=['GET'])
def userDelfunc(q):
    res = process_header('_userDel',q)
    return res

if (__name__ == "__main__"):
    app.debug = True
    app.run(port = 3020)