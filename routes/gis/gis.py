from module.controller.headerque import process_header
from module.controller.jwtGen import *
from flask import Blueprint
from routes.static import ver
import requests
from flask import Flask, request, jsonify

gis = Blueprint('gis',__name__)


@gis.route('/api/{ver}/que/gis/<id>'.format(ver=ver), methods=['GET'])
def gismap(id):
    res = process_header('_apiGis',id)
    return res
