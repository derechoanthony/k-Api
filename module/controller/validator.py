import sys, os
import jwt
import time
import datetime
from con import *


class checkExp(object):
    flag = False # 
    def __init__(self,t):
        self.t = t
    def current(self):
        n = datetime.datetime.now()
        unix_time = time.mktime(n.timetuple())
        return int(unix_time)
    def isExpired(self):
        return int(self.current()) > int(self.t)
        
class validateJwt(object):
    def __init__(self,arg):
        self.arg = arg
        self.uid = self.arg['uid'] # User ID
        self.exp = self.arg['exp'] # Reg Expiration Date
        self.isExp = checkExp(self.exp)
        self.chkExp = checkExp.isExpired(self.isExp)
    def validateResult(self):
        data = {}
        data["code"] = "200"
        if self.chkExp == True and self.uid !="":
            data["code"] = "203"
            data["msg"] = "nable to process request, session already expired!"
        data["data"] = self.arg
        return data

def getToken(s, seps):
    res = [s]
    for sep in seps:
        s, res = res, []
        for seq in s:
            res += seq.split(sep)
    d = jwt.decode(res[1], verify=False)
    d['token'] = res[1]
    getJwt = validateJwt(d)
    jwtValidation = validateJwt.validateResult(getJwt)
    return jwtValidation
    
def queid(j):
    stmt = select([usrTable.c.usrid]).where(usrTable.c.username==j["uname"]).where(usrTable.c.pwd==j["pwd"]).order_by(usrTable.c.usrid)
    return [dict(zip(r.keys(), r)) for r in conn.engine.execute(stmt).fetchall()]