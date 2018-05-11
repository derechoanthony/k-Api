import json
from module.controller.con import *
from module.controller.validator import queid
from .user import userNewAccess

class vendor(object):
    def __init__(self,arg=None,data=None,q=None):
        self.arg = arg
        self.data = data
        self.q = q
    def regVendor(self):
        data = {}
        res = {}
        usr = {}
        data['fname'] = self.arg['ContactPerson'][0]['Fname']
        data['lanme'] = self.arg['ContactPerson'][0]['Lname']
        data['address'] = self.arg['Address']
        data['mobile'] = self.arg['Contact'][0]['mobile']
        data['tel'] = self.arg['Contact'][0]['tel']
        data['email'] = self.arg['Email']
        data['payment'] = self.arg['Payment-Type']
        data['CompanyName'] = self.arg['CompanyName']
        # data['pwd'] = self.arg['pwd']
        # data['role'] = self.arg['role']

        usr['username'] = self.arg['Email']
        usr['pwd'] = self.arg['pwd']
        usr['email'] = self.arg['Email']
        usr['contact'] = "M-{mobile}|T-{tel}".format(mobile=self.arg['Contact'][0]['mobile'],tel=self.arg['Contact'][0]['tel'])
        usr['firstname'] = self.arg['ContactPerson'][0]['Fname']
        usr['lastname'] = self.arg['ContactPerson'][0]['Lname']
        usr['usrrole'] = [self.arg['role']]
        newuser = userNewAccess(usr)
        # print("----------->{}".format(newuser['code']))

        if newuser['code'] == "200":
            try:
                stmnt = ven.insert().values(data)
                vendor_result = conn.execute(stmnt)
                res["code"] = "200"
                res['data'] = [{"vendorid":vendor_result.inserted_primary_key}]
                res['msg'] = "New vendor successfully created!"
            except Exception as e:
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOGx:{db_name} - {e}".format(e=e,db_name="vendor")
        else:
            # print("data code: 203")
            res["coce"] = "203"
            res["data"] = []
            res['msg'] = "Vendor already exist!"
        

        
        return res
    
    def updateVendor(self):
        data = {}
        res = {}
        ven_id = self.q
        data['fname'] = self.arg['ContactPerson'][0]['Fname']
        data['lanme'] = self.arg['ContactPerson'][0]['Lname']
        data['address'] = self.arg['Address']
        data['mobile'] = self.arg['Contact'][0]['mobile']
        data['tel'] = self.arg['Contact'][0]['tel']
        data['email'] = self.arg['Email']
        data['payment'] = self.arg['Payment-Type']
        data['CompanyName'] = self.arg['CompanyName']

        try:
            stmnt = ven.update().values(data).where(ven.c.ven_id==ven_id)
            vendor_result = conn.execute(stmnt)
            if vendor_result.rowcount == 1:
                res["code"] = "200"
                res['data'] = []
                res['msg'] = "Vendor id {id} successfully Update!".format(id=ven_id)
            else:
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOG:{db_name} - {e}".format(e="something went wrong on the db",db_name="vendor")
        except Exception as e:
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="vendor")
        return res

    def VendorList(self):
        res ={}
        stmt = select([ven]).where(ven.c.status == 1)
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
    def VendorListinactive(self):
        res ={}
        stmt = select([ven]).where(ven.c.status == 0)
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
    def SingleVendorList(self):
        res ={}
        stmt = select([ven]).where(ven.c.status == 1)
        stmt = stmt.where(ven.c.ven_id == self.q)
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
    def deactivatevendor(self):
        res = {}
        data ={}
        data['status'] = 0
        try:
            stmt = ven.update().values(data).where(ven.c.ven_id == self.arg['id'])
            vendor_result = conn.execute(stmt)
            if vendor_result.rowcount == 1:
                res["code"] = "200"
                res['data'] = []
                res['msg'] = "Vendor id {id} successfully Deactivate!".format(id = self.arg['id'])
            else:
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOG:{db_name} - {e}".format(e="something went wrong on the db",db_name="vendor")
        except Exception as e:
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="vendor")
        return res
    def activatevendor(self):
        res = {}
        data ={}
        data['status'] = 1
        try:
            stmt = ven.update().values(data).where(ven.c.ven_id == self.arg['id'])
            vendor_result = conn.execute(stmt)
            if vendor_result.rowcount == 1:
                res["code"] = "200"
                res['data'] = []
                res['msg'] = "Vendor id {id} successfully Activate!".format(id = self.arg['id'])
            else:
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOG:{db_name} - {e}".format(e="something went wrong on the db",db_name="vendor")
        except Exception as e:
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="vendor")
        return res


        
