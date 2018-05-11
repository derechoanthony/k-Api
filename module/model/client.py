import json
from module.controller.con import *
from module.controller.validator import queid



class clientApi(object):

    def __init__(self, arg = None, data = None, queid = None):

        self.arg = arg
        self.data = data
        self.queid = queid


    def newCLientEntry(self):
        res = {}
        self.detail = self.arg
        self.detail["status"] = 1
        check = checkEntry(self.detail["email"])
        if check == True:
            nclient = client.insert().values(self.detail)
            s = conn.execute(nclient)

            res['code'] = "200"
            res['email'] = self.detail["email"]
            res['msg'] = "Successfully created new client"
        else:
            res['code'] = "202"
            res['email'] = res['email'] = self.detail["email"]
            res['msg'] = "Email is already exist"
        return res



    def getClientActiveList(self):
        res = {}
        client_list = select([client]).where(client.c.status==1)
        data = [dict(zip(r.keys(), r)) for r in conn.execute(client_list).fetchall()]
        if len(data) == 0:
            res["code"] = "204"
            res["data"] = []
            res["msg"] = "No active client found!"
        else:
            res["code"] = "200"
            res["data"] = data
            res["msg"] = "ok"
        return res

    
    def getClientInactiveList(self):
        res = {}
        client_list = select([client]).where(client.c.status==0)
        data = [dict(zip(r.keys(), r)) for r in conn.execute(client_list).fetchall()]
        if len(data) == 0:
            res["code"] = "204"
            res["data"] = []
            res["msg"] = "No inactive client found!"
        else:
            res["code"] = "200"
            res["data"] = data
            res["msg"] = "ok"
        return res



    def updateClient(self):

        res = {}
        self.detail = self.arg["data"][0]
        self.detail["client_id"] = self.arg["client_id"]

        try:
            chck_id = select([client]).where(client.c.client_id == self.detail["client_id"])
            res_check_id = conn.execute(chck_id)
            if res_check_id.rowcount == 1:
                print("naa gyud")
                try: 
                    update_client = client.update().values(self.detail).where(client.c.client_id==self.detail["client_id"])
                    # data = [dict(zip(r.keys(), r)) for r in conn.execute(uclient).fetchall()]
                    res_update_client = conn.execute(update_client)

                    res["code"] = "200"
                    res["booking_id"] = self.detail["client_id"]
                    res["msg"] = "Successfully update"
                except Exception as e:
                    res["code"] = "202"
                    res["msg"] = "Failed update"

            else:
                res["code"] = "204"
                res["id"] = self.detail["client_id"]
                res["msg"] = "No client found!"
        
        except Exception as e:
            res["code"] = "400"
            res["msg"] = "Bad request"

        return res

    
    def deactivateClient(self):
        res = {}
        try:
            check_status = select([client]).where(client.c.client_id==self.queid).where(client.c.status==0)
            res_check = conn.execute(check_status)
            if res_check.rowcount == 1:
                res["code"] = "202"
                res["id"] = self.queid 
                res["msg"] = "already deactivated"
                
            else:
                deactivate_client = client.update().where(client.c.client_id==self.queid).values(status=0)
                res_deactivate = conn.execute(deactivate_client)

                res["code"] = "200"
                res["id"] = self.queid 
                res["msg"] = "Successfully deactivated"
        except Exception as e:
            res["code"] = "204"
            res["id"] = q 
            res["msg"] = "Unable to deactivate"
        
        return res



    def activateClient(self):
        res = {}
        try:
            check_status = select([client]).where(client.c.client_id==self.queid).where(client.c.status==1)
            res_check = conn.execute(check_status)
            if res_check.rowcount == 1:
                res["code"] = "202"
                res["id"] = self.queid
                res["msg"] = "already activated"
                
            else:
                deactivate_client = client.update().where(client.c.client_id==self.queid).values(status=1)
                res_deactivate = conn.execute(deactivate_client)

                res["code"] = "200"
                res["id"] = self.queid
                res["msg"] = "Successfully activate"
        except Exception as e:
            res["code"] = "204"
            res["id"] = self.queid
            res["msg"] = "Unable to activate"
        
        return res



    def singleSearch(self):
        res = {}
        try:
            check_client = select([client.c.client_type, client.c.fname, client.c.lname, client.c.contact, client.c.email, client.c.address ]).where(client.c.client_id == self.queid)
            res_check_client = conn.execute(check_client)

            if res_check_client.rowcount == 1:
                data = [dict(zip(r.keys(), r)) for r in conn.execute(check_client).fetchall()]
                res["code"] = "200"
                res["id"] = data
                res["msg"] = "ok"

            else:
                res["code"] = "203"
                res["id"] = self.queid
                res["msg"] = "No client found"

        except Exception as e:
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Client")

        return res

    




def checkEntry(em):

    chck = select([client]).where(client.c.email==em)
    data = [dict(zip(r.keys(), r)) for r in conn.execute(chck).fetchall() ]
    if len(data) == 0:
        i = True
    else:
        i = False
    return i



    
# def deleteClient(j,q):
#     res = {}
#     try:

#         chck_client = select([client]).where(client.c.client_id==q)
#         res_chck = conn.execute(chck_client)

#         if res_chck.rowcount ==1:
#             delete_client = client.delete().where(client.c.client_id==q)
#             res_delete = conn.execute(delete_client)
#             res["code"] = "200"
#             res["client_id"] = q 
#             res["msg"] = "Successfully deleted"
#         else:
#             res['code'] = "203"
#             res["client_id"] = q 
#             res["msg"] = "Invalid client id"
        
#     except Exception as e:
#         res['code'] = "400"
#         res['msg'] = "Bad request"
#     return res