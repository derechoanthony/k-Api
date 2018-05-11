from module.controller.headerque import process_header
from module.controller.jwtGen import *
from flask import *
from flask import Blueprint

from routes.static import ver
import requests

# from flask import Flask, request, jsonify

clientapi = Blueprint('clientapi', __name__)

@clientapi.route('/api/{ver}/client/entry'.format(ver=ver), methods=['POST'])
def clientEntry():
    res = process_header("_clientEntry")
    return res

@clientapi.route('/api/{ver}/client/active/list'.format(ver=ver), methods=['GET'])
def clientActiveList():
    res = process_header("_clientActiveList")
    return res


@clientapi.route('/api/{ver}/client/inactive/list'.format(ver=ver), methods=['GET'])
def clientInactiveList():
    res = process_header("_clientInactiveList")
    return res

@clientapi.route('/api/{ver}/client/update'.format(ver=ver), methods=['POST'])
def clientUpdate():
    res = process_header("_clientUpdate")
    return res


@clientapi.route('/api/{ver}/client/deactivate/<q>'.format(ver=ver), methods=['GET'])
def clientDeactivate(q):
    res = process_header("_clientDeactivate", q)
    return res

@clientapi.route('/api/{ver}/client/activate/<q>'.format(ver=ver), methods=['GET'])
def clientActivate(q):
    res = process_header("_clientActivate", q)
    return res


@clientapi.route('/api/{ver}/client/single/search/<q>'.format(ver=ver), methods=['GET'])
def clientSearch(q):
    res = process_header("_clientSearch", q)
    return res   

# @clientapi.route('/api/{ver}/client/delete/<q>'.format(ver=ver), methods=['GET'])
# def bookingDelete(q):
#     res = process_header("_clientDelete", q)
#     return res