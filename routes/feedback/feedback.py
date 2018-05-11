from module.controller.headerque import process_header
from module.controller.jwtGen import *
from flask import Blueprint, send_file
from routes.static import ver
import requests
import base64
import sys
from flask import Flask, request, jsonify
print(ver)

feedback = Blueprint('feedback', __name__)

# insert ratings
@feedback.route('/api/{ver}/insert/ratings'.format(ver=ver), methods=['POST'])
def apprating():
    res = process_header('_apratings')
    return res

# get all rating by vendor id
@feedback.route('/api/{ver}/get/all/rating/<id>'.format(ver=ver), methods=['GET'])
def apallrating(id):
    res = process_header('_appallrating',id)
    return res

# get all  rating by vehicle id
@feedback.route('/api/{ver}/get/vehicle/rating/<id>'.format(ver=ver), methods=['GET'])
def apavehicle(id):
    res = process_header('_apavehicle', id)
    return res

# insert reviews
@feedback.route('/api/{ver}/insert/reviews'.format(ver=ver), methods=['POST'])
def apreviewsEntry():
    res =  process_header('_appreviewsEntry')
    return res

# get all reveviews by vendor id
@feedback.route('/api/{ver}/get/all/review/<id>'.format(ver=ver), methods=['GET'])
def apallreview(id):
    res = process_header('_apallreview', id)
    return res

# get all review by vehicle id
@feedback.route('/api/{ver}/get/vehicle/review/<id>'.format(ver=ver), methods=['GET'])
def apavehiclereview(id):
    res = process_header('_apavehiclereview', id)
    return res