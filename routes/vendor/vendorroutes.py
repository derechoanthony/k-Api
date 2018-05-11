from module.controller.headerque import process_header,process_Frontend
from module.controller.jwtGen import *
from flask import Blueprint
from routes.static import ver
import requests
from flask import Flask, request, jsonify

vendorapi = Blueprint('vendorapi',__name__)

@vendorapi.route('/api/{ver}/new/vendor'.format(ver=ver), methods=['POST'])
def appvendorcreate():
    res = process_Frontend('_vendorcreate')
    return res
@vendorapi.route('/api/{ver}/vendor/update/<querystring>'.format(ver=ver), methods=['POST'])
def appvendorupdate(querystring):
    res = process_header('_vendorupdate',querystring)
    return res
@vendorapi.route('/api/{ver}/vendor/list'.format(ver=ver), methods=['GET'])
def appVendorList():
    res = process_header('_vendorlist')
    return res

@vendorapi.route('/api/{ver}/vendor/list/<querystring>'.format(ver=ver), methods=['GET'])
def appvendorlistSingle(querystring):
    res = process_header('_vendorlistsingle',querystring)
    return res
@vendorapi.route('/api/{ver}/vendor/deactivate'.format(ver=ver), methods=['POST'])
def appvendordeactivate():
    res = process_header('_vendordeactivate')
    return res
@vendorapi.route('/api/{ver}/vendor/activate'.format(ver=ver), methods=['POST'])
def appvendoractivate():
    res = process_header('_vendoractivate')
    return res
@vendorapi.route('/api/{ver}/vendor/list/inactive'.format(ver=ver), methods=['GET'])
def appvendorinactive():
    res = process_header('_vendorinactive')
    return res