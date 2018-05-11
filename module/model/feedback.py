import json
import pymongo
from module.controller.con import *
from module.controller.validator import queid
from pymongo import MongoClient
from config import MDB
from bson import BSON
from bson import json_util

class feedback(object):
    def __init__(self, arg):
        self.arg =  arg

    def ratingentry(self):
        res = {}
        try:
            insert = rating.insert().values(self.arg)
            rating_insert = conn.execute(insert)
            
            if rating_insert.rowcount == 1:
                res["code"] = "200"
                res['success'] = True
                res['msg'] = 'rating successfully inserted!'

        except Exception as e:
            res["code"] = "203"
            res['success'] = False
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e, db_name="rating")
        return res

    def reviewsEntry(self):
        res = {}
        try:
            insert = review.insert().values(self.arg)
            rating_insert = conn.execute(insert)

            if rating_insert.rowcount == 1:
                res["code"] = "200"
                res['success'] = True
                res['msg'] = 'rating successfully inserted!'

        except Exception as e:
            res["code"] = "203"
            res['success'] = False
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e, db_name="rating")
        return res
    
    def allrating(self):
        res={}
        try:
            que = select([rating]).where(rating.c.vendor_id == self.arg)
            d = [dict(zip(r.keys(), r)) for r in conn.engine.execute(que).fetchall()]
            if len(d) == 0:
                res["code"] = "204"
                res["data"] = []
                res["msg"] = "No content found!"
            else:
                res["code"] = "200"
                res["data"] = d
                res["msg"] = "ok"
            return res
        except Exception as e:
            res["code"] = "204"
            res["data"] = []
            res["msg"] = "No content found!"
        return res

    def allreview(self):
        res = {}
        try:
            que = select([review]).where(review.c.vendor_id == self.arg)
            d = [dict(zip(r.keys(), r))
                 for r in conn.engine.execute(que).fetchall()]
            if len(d) == 0:
                res["code"] = "204"
                res["data"] = []
                res["msg"] = "No content found!"
            else:
                res["code"] = "200"
                res["data"] = d
                res["msg"] = "ok"
            return res
        except Exception as e:
            res["code"] = "204"
            res["data"] = []
            res["msg"] = "No content found!"
        return res

    def vehiclerating(self):
        res={}
        try:
            que = select([rating]).where(rating.c.vehicle_id == self.arg)
            d = [dict(zip(r.keys(), r)) for r in conn.engine.execute(que).fetchall()]
            if len(d) == 0:
                res["code"] = "204"
                res["data"] = []
                res["msg"] = "No content found!"
            else:
                res["code"] = "200"
                res["data"] = d
                res["msg"] = "ok"
            return res
        except Exception as e:
            res["code"] = "204"
            res["data"] = []
            res["msg"] = "No content found!"
        return res

    def vehiclereview(self):
        res = {}
        try:
            que = select([review]).where(review.c.vehicle_id == self.arg)
            d = [dict(zip(r.keys(), r))
                 for r in conn.engine.execute(que).fetchall()]
            if len(d) == 0:
                res["code"] = "204"
                res["data"] = []
                res["msg"] = "No content found!"
            else:
                res["code"] = "200"
                res["data"] = d
                res["msg"] = "ok"
            return res
        except Exception as e:
            res["code"] = "204"
            res["data"] = []
            res["msg"] = "No content found!"
        return res
    
