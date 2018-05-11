from module.controller.headerque import process_header
from module.controller.jwtGen import *
from flask import Blueprint, send_file
from routes.static import ver
import requests
from flask import Flask, request, jsonify
from config import IMG_PATH

vehicleapi = Blueprint('vehicleapi',__name__)

@vehicleapi.route('/api/{ver}/new/vehicle/entry'.format(ver=ver), methods=['POST'])
def appvehicleentry():
    res = process_header('_vehiclecreate')
    return res
@vehicleapi.route('/api/{ver}/vehicle/update/<q>'.format(ver=ver), methods=['POST'])
def apivehicleupdate(q):
    res = process_header('_vehicleupdate',q)
    return res
@vehicleapi.route('/api/{ver}/vehicle/single/search/<q>'.format(ver=ver), methods=['GET'])
def apisinglesearch(q):
    res = process_header('_apisinglesearch',q)
    return res


@vehicleapi.route('/api/{ver}/vehicle/req/deactivate'.format(ver=ver), methods=['POST'])
def apivehicle_reqDeactivate():
    res = process_header('_vehiclereqdeactivate')
    return res
@vehicleapi.route('/api/{ver}/vehicle/deactivate/list'.format(ver=ver), methods=['GET'])
def apivehicledeactivatelist():
    res = process_header('_apivehicledeactivatelist')
    return res
@vehicleapi.route('/api/{ver}/vehicle/list'.format(ver=ver), methods=['GET'])
def apivehicle__vehiclelist():
    res = process_header('_apivehiclelist')
    return res

@vehicleapi.route('/api/{ver}/vehicle/app/deactivate'.format(ver=ver), methods=['POST'])
def apivehicle_appDeactivate():
    res = process_header('_apivehicle_appDeactivate')
    return res
@vehicleapi.route('/api/{ver}/vehicle/activate'.format(ver=ver), methods=['POST'])
def apivehicle_activate():
    res = process_header('_apivehicle_activate')
    return res


@vehicleapi.route('/api/{ver}/vehicle/get_image/<data>'.format(ver=ver), methods=['GET'])
def get_image(data):
    vfile = '{imagepath}/{data}'.format(data=data, imagepath=IMG_PATH)
    print(vfile)
    return send_file(vfile, mimetype='image/jpeg')
