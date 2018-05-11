from module.controller.headerque import process_header
from module.controller.jwtGen import *
from flask import Blueprint
from routes.static import ver
import requests
from flask import Flask, request, jsonify
userapi = Blueprint('userapi',__name__)
#---------------------------------------------------------------------------------------------------------------------------------[User Role]
@userapi.route('/api/{ver}/user/role'.format(ver=ver), methods=['GET'])
def appuserrole():
    res = process_header('_userrole')
    return res
#---------------------------------------------------------------------------------------------------------------------------------[End of User Role]
#---------------------------------------------------------------------------------------------------------------------------------[Back Office:User's]
#login 
@userapi.route('/api/{ver}/user/login'.format(ver=ver), methods=['POST'])
def appgettoken():
    json_input = request.json if type(request.json).__name__=='dict' else request.json
    h = genJWT(json_input)
    res = genJWT.jwtGenData(h)
    return res
#version controller
@userapi.route('/api/version/controller', methods=['GET'])
def appget_ver():
    return ver
#update  user
@userapi.route('/api/{ver}/edit/user/account'.format(ver=ver), methods=['POST'])
def appuserEditfunc():
    res = process_header('_userEdit')
    return res
@userapi.route('/api/{ver}/remove/user/account/<q>'.format(ver=ver), methods=['GET'])
def appuserDelfunc(q):
    res = process_header('_userDel',q)
    return res
@userapi.route('/api/{ver}/search/single/user/access/<querystring>'.format(ver=ver), methods=['GET'])
def appsingleuserque(querystring):
    res = process_header('_singleUserSearch',querystring)
    return res
@userapi.route('/api/{ver}/user/list'.format(ver=ver), methods=['GET'])
def appuserlist():
    res = process_header('_usrlist')
    return res

@userapi.route('/api/{ver}/user/entry'.format(ver=ver), methods=['POST'])
def appcreate_user():
    res = process_header('_userEntryData')
    return res
@userapi.route('/api/{ver}/new/user/access'.format(ver=ver), methods=['POST'])
def appcreate_user_access():
    res = process_header('_userNewAccess')
    return res
@userapi.route('/api/{ver}/activate/user'.format(ver=ver), methods=['POST'])
def appuserActivation():
    res = process_header('_appuseractivate')
    return res
#---------------------------------------------------------------------------------------------------------------------------------[End of Back Office:User's] 

#---------------------------------------------------------------------------------------------------------------------------------[Back Office:Quoatation]
@userapi.route('/api/{ver}/new/quote'.format(ver=ver), methods=['POST'])
def appQuoate():
    res = process_header('_createQuoate')
    return res
@userapi.route('/api/{ver}/quote/list'.format(ver=ver), methods=['GET'])
def QuoteList():
    res = process_header('_Qlist')
    return res
@userapi.route('/api/{ver}/quote/single/list/<q>'.format(ver=ver), methods=['GET'])
def QuotesingleList(q):
    res = process_header('_Qslist',q)
    return res
@userapi.route('/api/{ver}/update/quote/<querystring>'.format(ver=ver), methods=['POST'])
def appQuoateUpdate(querystring):
    res = process_header('_Qupdate',querystring)
    return res
#---------------------------------------------------------------------------------------------------------------------------------[End of Back Office:Quoatation]
#---------------------------------------------------------------------------------------------------------------------------------[Back Office:Invoice]
@userapi.route('/api/{ver}/new/invoice'.format(ver=ver), methods=['POST'])
def appInvoice():
    res = process_header('_createinvoice')
    return res
#---------------------------------------------------------------------------------------------------------------------------------[End of Back Office:Invoice]

