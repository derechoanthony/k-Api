import json
import pymongo
from module.controller.con import *
from module.controller.validator import queid
from pymongo import MongoClient
from config import MDB
from bson import BSON
from bson import json_util


src = MDB['source']
port = MDB['port']

class GIS(object):
    def __init__(self, args):
        self.arg = args
        self.client = MongoClient(src, port)
        self.db = self.client.geo
        self.collection = self.db.coordinates
    def getGis(self):
        docs = []
        data = {}
        print({"bookingID": "{id}".format(id=self.arg)})
        for collection in self.collection.find({"bookingID":"{}".format(self.arg)}):
            collection.pop('_id')
            collection.pop('token')
            docs.append(collection)
        return docs
    
