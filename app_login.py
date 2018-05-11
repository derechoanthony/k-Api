from module.controller.jwtGen import *
from flask import *
import requests

app = Flask(__name__)

@app.route('/api/v1.0/user/login', methods=['POST'])
def gettoken():
    json_input = request.json if type(request.json).__name__=='dict' else request.json
    h = genJWT(json_input)
    res = genJWT.jwtGenData(h)
    return res
if (__name__ == "__main__"):
    app.debug = True
    app.run(port = 3000)