import jwt
import json
from flask import Flask, request, jsonify
import requests

file = open("curver.log","r")
d = file.read()
decrypt = jwt.decode(d, verify=False)
ver = decrypt["ver"]

app = Flask(__name__)
@app.route('/api/version/controller', methods=['GET'])
def get_ver():
    return ver

if (__name__ == "__main__"):
    app.debug = True
    app.run(port = 2010)
