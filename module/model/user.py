import json
from module.controller.con import *
from module.controller.validator import queid

def UserEntry(j,d=None):
    
    return j
def userNewAccess(j,d=None):
    print(j)
    data = {}
    res = {}
    data['uname'] = j["username"]
    data['pwd'] = j["pwd"]
    if len(queid(data)) >=1:
        res["code"] = "203"
        res["data"] = []
        res["msg"] = "user is already exist"
    else:
        res = insertUserAccess(j, d=None)
    return res
def insertUserAccess(j,d=None):
    d_result = {}
    username = j["username"]
    pwd = j["pwd"]
    firstname = j["firstname"]
    lastname = j["lastname"]
    email = j["email"]
    contact = j["contact"]
    if d == None:
        created = 0
    else:
        created = d['uid']
    usrrole = j['usrrole']
    try:
        i = usrTable.insert().values(username=username,pwd=pwd)
        result = conn.execute(i)
        try:
            usrid = result.inserted_primary_key
            i_p = usrProfile.insert().values(firstname=firstname,lastname=lastname,email=email,contact=contact,created=created,usrid=usrid)
            i_p_result = conn.execute(i_p)
            try:
                permit_d=[]
                for cnt in range(len(usrrole)):
                    i_per = userpermit.insert().values(permit_val=usrrole[cnt],userid=usrid)
                    i_per_result = conn.execute(i_per)
                    permit_d.append(i_per_result.inserted_primary_key[0])
                d_result['code'] = "200"
                d_result['data'] = [{"uid":usrid},{"profile-uid":i_p_result.inserted_primary_key},{"permit-uid":permit_d}]
                d_result['msg'] = "successfully created new user access"
            except Exception as e:
                d_result['code'] = "203"
                d_result['data'] = []
                d_result['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="userpermit")
        except Exception as e:
            d_result['code'] = "203"
            d_result['data'] = []
            d_result['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="userprofile")
    except Exception as e:
        d_result['code'] = "203"
        d_result['data'] = []
        d_result['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="usr")
    
    return d_result




    
def userSingleSearch(j,q):
    stmt = select([usrProfile]).where(usrProfile.c.usrid==q)
    res = {}
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

def multipleSearch():
    stmt = select([usrProfile.c.firstname,usrProfile.c.lastname,usrProfile.c.email,usrProfile.c.usrid])
    res = {}
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
def getUserRole():
    stmt = select([usrrole.c.role_name,usrrole.c.role_code]).where(usrrole.c.role_status=='1')
    print stmt
    res = {}
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


def userEdit(j):
    usrid = j["uid"]
    data = j["data"]
    

    username = data[0]["username"]
    pwd = data[0]["pwd"]

    firstname = data[0]["firstname"]
    lastname = data[0]["lastname"]
    email = data[0]["email"]
    usrrole = data[0]["usrrole"]
    contact = data[0]["contact"]

    d = {}
    try:
        stmt = usrTable.update().values(username=username,pwd=pwd).where(usrTable.c.usrid==usrid)
        res_acss = conn.execute(stmt)
        if res_acss.rowcount == 1:
            try:
                stmt_prof = usrProfile.update().values(firstname=firstname,lastname=lastname,email=email,contact=contact).where(usrProfile.c.usrid==usrid)
                res_prof = conn.execute(stmt_prof)
                if res_prof.rowcount == 1:
                    stmt_del_role = userpermit.delete().where(userpermit.c.userid==usrid)
                    conn.execute(stmt_del_role)
                    for cnt in range(len(usrrole)):
                        print usrrole[cnt]
                        stmt_role = userpermit.insert().values(permit_val=usrrole[cnt],userid=usrid)
                        conn.execute(stmt_role)
                    d["code"] = "200"
                    d["msg"] = "ok"
                    d["data"] = []
                else:
                    d["code"] = "204"
                    d["msg"] = "Unable to edit user profile! UID : {uid} Not Found!".format(uid=usrid)
                    d["data"] = []
            except Exception as e:
                d["code"] = "203"
                d["msg"] = e
                d["data"] = []
        else:
            d["code"] = "204"
            d["msg"] = "Unable to edit user access! UID : {uid} Not found!".format(uid=usrid)
            d["data"] = []        
    except Exception as e:
        d["code"] = "203"
        d["msg"] = e
        d["data"] = []
    
    # print 
    return d
def userDel(j,q):
    stmt_del_role = userpermit.delete().where(userpermit.c.userid==q)
    stmt_del_profile = usrProfile.delete().where(usrProfile.c.usrid==q)
    stmt_del_usr = usrTable.delete().where(usrTable.c.usrid==q)
    res ={}
    res_usr_del = conn.execute(stmt_del_usr)
    res_prof = conn.execute(stmt_del_profile)
    res_role = conn.execute(stmt_del_role)
    res["code"] = "200"
    res["msg"] = "successfully deleted!"
    res["data"] = []
    return res
    
def userUpdateAccess(j,q):
    pass

def userActivate(j,q):
    uid = j['id']
    try:
        stmt_usr = usrTable.update()
        stmt_usr = stmt_usr.values(usr_status="1")
        stmt_usr = stmt_usr.where(usrTable.c.usrid == uid)
        res_usr = conn.execute(stmt_usr)
        if res_usr.rowcount == 1:
            pass
        else:
            d["code"] = "204"
            d["msg"] = "Unable to activate! UID : {uid} Not Found!".format(id=usrid)
    except Exception as e:
        d["code"] = "203"
        d["msg"] = e    
    return d
    
