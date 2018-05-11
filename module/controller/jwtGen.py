from con import *
from module.model.user import userSingleSearch
import jwt
import sys, os
import time
import datetime

class genJWT(object):
    flag = False
    def __init__(self, arg):
        self.arg = arg
        self.uname = self.arg["uname"]
        self.pwd = self.arg["pwd"]
    
    def jwtGenData(self):
        """
            Note:
                ENCODED value: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZXNzYWdlIjoiTmV3IFRva2VuIEdlbmVyYXRlZCEiLCJjb2RlIjoiMjAwIiwiZGF0YSI6W3sidWlkIjoiMSIsImV4cCI6MTUyMTQ4MjUzNC44Mjg1Njh9XX0.hsh6wTOQ9tBehC8wiWERJcZKuEdWESDXLVnvP1SQLy4
                DECODED value:
                                {"uid": "1","exp": 1521482534}
                algorithm='HS256'
                secret = b64   
                exp = current_time + 5 minutes
                    equation: 
                            1 min = 60 sec
                            so...
                                t = 5 * 60
                                t = 300
        """
        self.d = {}
        self.q = self.queuser()  
        
        if len(self.q) == 0:
            self.d["uid"] = ""
            self.d["exp"] = int(time.time()+0)
        else:
            profile = userSingleSearch("",self.q[0]['usrid'])
            self.id=self.q[0]['usrid']
            self.d["uid"] = self.id
            self.d["profile"] = profile["data"]
            #original value: 300
            self.d["exp"] = int(time.time()+86400)
        self.encoded = jwt.encode(self.d, 'secret', algorithm='HS256')
        return self.encoded

    def queuser(self):
        stmt = select([usrTable.c.usrid]).where(usrTable.c.username==self.uname).where(usrTable.c.pwd==self.pwd).order_by(usrTable.c.usrid)
        return [dict(zip(r.keys(), r)) for r in conn.engine.execute(stmt).fetchall()]
    

# class module for data user
