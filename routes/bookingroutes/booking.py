from module.controller.headerque import process_header
from module.controller.jwtGen import *
from flask import *
from flask import Blueprint

from routes.static import ver
import requests
# from flask import Flask, request, jsonify

bookingapi = Blueprint('bookingapi', __name__)

@bookingapi.route('/api/{ver}/booking/entry'.format(ver=ver), methods=['POST'])
def bookingEntry():

    res = process_header("_bookingEntry")
    return res

@bookingapi.route('/api/{ver}/booking/active/list/<query>'.format(ver=ver), methods=['GET'])
def bookingList(query):
    res = process_header("_bookingActiveList", query)
    return res

@bookingapi.route('/api/{ver}/booking/active/list'.format(ver=ver), methods=['GET'])
def bookingActList():
    res = process_header("_bookingActiveList")
    return res



@bookingapi.route('/api/{ver}/booking/inactive/list'.format(ver=ver), methods=['GET'])
def bookingInactiveList():

    res = process_header("_bookingInactiveList")
    return res


@bookingapi.route('/api/{ver}/booking/update'.format(ver=ver), methods=['POST'])
def bookingUpdate():
    res = process_header("_bookingUpdate")
    return res


@bookingapi.route('/api/{ver}/booking/search/<q>'.format(ver=ver), methods=['GET'])
def searchBook(q):
    res = process_header("_singleSearch", q)
    return res


@bookingapi.route('/api/{ver}/booking/deactivate/<q>'.format(ver=ver), methods=['GET'])
def bookingDeactivate(q):
    res = process_header("_bookingDeactivate", q)
    return res



@bookingapi.route('/api/{ver}/booking/activate/<q>'.format(ver=ver), methods=['GET'])
def bookingActivate(q):
    res = process_header("_bookingActivate", q)
    return res



# @bookingapi.route('/api/{ver}/booking/delete/<q>'.format(ver=ver), methods=['GET'])
# def bookingDelete(q):
#     res = process_header("_bookingDelete", q)
#     return res


@bookingapi.route('/api/{ver}/booking/block/date'.format(ver=ver), methods=['POST'])
def bookingBlock():
    res = process_header("_bookingBlock")
    return res
