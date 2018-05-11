import json
import base64
from module.controller.con import *
from module.controller.validator import queid
from config import IMG_PATH

class vehicle(object):
    def __init__(self,arg=None,data=None,q=None):
        self.arg = arg
        self.data = data
        self.q = q

    def regVehicle(self):

        detail = {}
        res = {}
        detail = self.arg['vehicle_data'][0]
        plate = detail['platenumber']
        detail['vendor_id'] = self.arg['vendor_id']
        
        images = detail.pop('images')
        imgcount = len(images)
        detail['imgcount'] = imgcount
        
        try:
            stmnt = vehcle.insert().values(detail)
            vehicle_result = conn.execute(stmnt)

            res["code"] = "200"
            res['data'] = [{"vehicle id":vehicle_result.inserted_primary_key}]
            res['msg'] = "New vehicle successfully created!"
            for i in range(imgcount):
                imagedata = images[i]['img-codex']
                imageString = imagedata.split(',')
                image_64_decode = base64.decodestring(imageString[1])
                fname = "{id}_{cnt}".format(id=plate, cnt=i)
                fh = open('{imagepath}/{filename}'.format(filename=fname,imagepath=IMG_PATH), "wb")
                fh.write(image_64_decode)
                fh.close

        except Exception as e:
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="vendor")
            
        return res
    def updateVehicle(self):
        detail = {}
        res = {}
        detail = self.arg['vehicle_data'][0]
        detail['vendor_id'] = self.arg['vendor_id']
        vehicle_id = self.q
        try:
            stmnt = vehcle.update().values(detail).where(vehcle.c.vehicle_id == vehicle_id)
            vehicle_result = conn.execute(stmnt)
            if vehicle_result.rowcount == 1:
                res["code"] = "200"
                res['data'] = []
                res['msg'] = "Vehicle id {id} successfully Update!".format(id=vehicle_id)
            else:
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOG:{db_name} - {e}".format(e="something went wrong on the db",db_name="Vehicle")

        except Exception as e:
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Vehicle")
        return res
    def reqDeactivate(self):
        data = {}
        res = {}
        data['req_deactivate'] = 1
        data['reason_deactivation'] = self.arg['particulars']
        vehicle_id = self.arg['id']

        try:
            stmnt = vehcle.update().values(data).where(vehcle.c.vehicle_id == vehicle_id)
            vehicle_result = conn.execute(stmnt)
            if vehicle_result.rowcount == 1:
                res["code"] = "200"
                res['data'] = []
                res['msg'] = "Vehicle id {id} request for deactivation!".format(id=vehicle_id)
            else:
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOG:{db_name} - {e}".format(e="something went wrong on the db",db_name="Vehicle")

        except Exception as e:
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Vehicle")
        return res

    def vehiclesiglelist(self):
        res = {}
        stmt = select([vehcle]).where(vehcle.c.status == 1)
        stmt = stmt.where(vehcle.c.vehicle_id==self.q)
        d = [dict(zip(r.keys(), r)) for r in conn.engine.execute(stmt).fetchall()]
        if len(d) == 0:
            res["code"] = "204"
            res["data"] = []
            res["msg"] = "No content found!"
        else:
            res["code"] = "200"
            res["data"] = d
            res["msg"] = "ok"
        return res
    def vehiclelist(self):
        res = {}
        stmt = select([vehcle]).where(vehcle.c.status == 1)
        d = [dict(zip(r.keys(), r)) for r in conn.engine.execute(stmt).fetchall()]
        if len(d) == 0:
            res["code"] = "204"
            res["data"] = []
            res["msg"] = "No content found!"
        else:
            res["code"] = "200"
            res["data"] = d
            res["msg"] = "ok"
        return res
    def vehicledeactivatelist(self):
        res = {}
        stmt = select([vehcle]).where(vehcle.c.status == 0)
        d = [dict(zip(r.keys(), r)) for r in conn.engine.execute(stmt).fetchall()]
        if len(d) == 0:
            res["code"] = "204"
            res["data"] = []
            res["msg"] = "No content found!"
        else:
            res["code"] = "200"
            res["data"] = d
            res["msg"] = "ok"
        return res
    def appDeactivate(self):
        data = {}
        res = {}
        data['status'] = 0
        vehicle_id = self.arg['id']

        try:
            stmnt = vehcle.update().values(data).where(vehcle.c.vehicle_id == vehicle_id)
            vehicle_result = conn.execute(stmnt)
            if vehicle_result.rowcount == 1:
                res["code"] = "200"
                res['data'] = []
                res['msg'] = "Vehicle id {id} successfully deactivation!".format(id=vehicle_id)
            else:
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOG:{db_name} - {e}".format(e="something went wrong on the db",db_name="Vehicle")

        except Exception as e:
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Vehicle")
        return res
    def activateVehicle(self):
        data = {}
        res = {}
        data['status'] =1
        vehicle_id = self.arg['id']

        try:
            stmnt = vehcle.update().values(data).where(vehcle.c.vehicle_id == vehicle_id)
            vehicle_result = conn.execute(stmnt)
            if vehicle_result.rowcount == 1:
                res["code"] = "200"
                res['data'] = []
                res['msg'] = "Vehicle id {id} successfully activated!".format(id=vehicle_id)
            else:
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOG:{db_name} - {e}".format(e="something went wrong on the db",db_name="Vehicle")

        except Exception as e:
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Vehicle")
        return res
