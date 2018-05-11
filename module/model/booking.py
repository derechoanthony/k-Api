import json
from module.controller.con import *
from module.controller.validator import queid
import random, time
from flask import Flask, request, jsonify
from datetime import date, datetime, timedelta


class bookingApi(object):

    def __init__(self, arg = None, data = None, queid = None):

        self.arg = arg
        self.data = data
        self.queid = queid


    

    def newBookingEntry(self):
        res = {}
        self.detail = {}
        self.block = {}
        
        # d = self.arg
        
        self.detail =  self.arg["data"][0] 
        self.detail["client_id"] = self.arg["client_id"]     
        self.detail["pointA"] = '{lat},{lon}'.format(lat = self.arg["location"][0]["pointA"][0], lon = self.arg["location"][0]["pointA"][1])    
        self.detail["pointB"] = '{lat},{lon}'.format(lat = self.arg["location"][0]["pointB"][0], lon = self.arg["location"][0]["pointB"][1])
        self.detail["status"] = 1
        self.detail["booking_code"] = hash_code() # get booking code
        time  = check_time(self.arg["data"][0]["start_date"], self.arg["data"][0]["end_date"])

       
        self.block["start_date"] = self.arg["data"][0]["start_date"]  
        self.block["end_date"] =  self.arg["data"][0]["end_date"]
        self.block["status"] = 1   
        self.block["time_consume"] = time
        self.block["vehicleID"] = self.arg["data"][0]["vehicleID"]   

        (sd,st) = self.detail["start_date"].split(" ")
        (ed,et) = self.detail["end_date"].split(" ")
       

        datetime_start= datetime.strptime(sd, '%Y-%m-%d')
        datetime_end= datetime.strptime(ed, '%Y-%m-%d')
        delta = datetime_end - datetime_start

        date_today = []
        for i in range(delta.days + 1):
            date = datetime_start + timedelta(days=i)
            date_today.append(date)
            
        try:
            check_booking = select([booking]).where(booking.c.vehicleID== self.block["vehicleID"])
            data_check_booking = conn.execute(check_booking).fetchall()
            res_check_booking = conn.execute(check_booking)

            if res_check_booking.rowcount >= 1:

                check_block_head = select([block_head]).where(block_head.c.vehicleID == self.block["vehicleID"])
                res_check_block_head = conn.execute(check_block_head)
                res_bh = conn.execute(check_block_head).fetchall()

                if res_check_block_head.rowcount >= 1:

                    res_block_head = chck_block_head(res_bh, self.block["start_date"] ,self.block["end_date"])

                    if res_block_head > 0:
                        res["code"] = "203"
                        res["msg"] = "not available this date"
                    else:
                        
                        res["booking_id"] = insert_booking(date_today, self.detail, self.block)
                        res["code"] = "200"
                        res["msg"] = "Successfully create booking "
                    
                else:
                    
                    res["booking_id"] = insert_booking(date_today, self.detail, self.block)
                    res["code"] = "200"
                    res["msg"] = "Successfully create booking "
            else:

                res["booking_id"] = insert_booking(date_today, self.detail, self.block)

                res["code"] = "200"
                res["msg"] = "Successfully create booking "
                
            
        except Exception as e:
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Booking")

        return res


    def updateBooking(self):
        res = {}
        self.detail = {}
        
        # d = self.arg
        
        self.detail =  self.arg["data"][0] 
        self.detail["bookingID"] = self.arg["bookingID"]
        self.detail["client_id"] = self.arg["client_id"]     
        self.detail["pointA"] = '{lat},{lon}'.format(lat = self.arg["location"][0]["pointA"][0], lon = self.arg["location"][0]["pointA"][1])    
        self.detail["pointB"] = '{lat},{lon}'.format(lat = self.arg["location"][0]["pointB"][0], lon = self.arg["location"][0]["pointB"][1])
        self.detail["status"] = 1

        try:
            chck_id = select([booking]).where(booking.c.bookingID == self.detail["bookingID"])
            res_check_id = conn.execute(chck_id)
            print(res_check_id.rowcount )
            if res_check_id.rowcount == 1:
                print("naa gyud")
                try: 
                    ubooking = booking.update().where(booking.c.bookingID == self.detail['bookingID']).values(self.detail)
                    # data = [dict(zip(r.keys(), r)) for r in conn.execute(uclient).fetchall()]
                    res_update_booking = conn.execute(ubooking)

                    res["code"] = "200"
                    res["booking_id"] = self.detail["bookingID"]
                    res["msg"] = "Successfully update"
                    
                except Exception as e:
                    res["code"] = "203"
                    res["msg"] = "Failed update"

            else:
                res["code"] = "204"
                res["id"] = self.detail["bookingID"]
                res["msg"] = "No booking found!"
        
        except Exception as e:
            res["code"] = "203"
            res["msg"] = "no booking found"

        return res
        


    def searchBooking(self):
        res = {}
        try:
            search = select([booking]).where(booking.c.bookingID == self.queid)    
            res_search = conn.execute(search)

            if res_search.rowcount == 1:
                data = [dict(zip(r.keys(), r)) for r in conn.execute(search).fetchall()]

                res["code"] = "200"
                res['data'] = data
                res["msg"] = "ok"
            else:

                res["code"] = "203"
                res['data'] = data
                res['msg'] = "No booking found"
                
        except Exception as e:   
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Booking")

        return res


    def getBookingActiveList(self):
        
        res = {}
        cd = datetime.today().strftime('%Y-%m-%d')
        
        if self.arg == "current":
            try:
                join_b_sb = outerjoin(booking, sub_booking, booking.c.bookingID == sub_booking.c.bookingID)
                stmt = select([booking]).select_from(join_b_sb).where(sub_booking.c.date_today == cd)
                data = [dict(zip(r.keys(), r)) for r in conn.execute(stmt).fetchall()]
                if len(data) > 0:
                    res["code"] = "200"
                    res["data"] = data
                    res["msg"] = "ok"
                else:
                    res["code"] = "203"
                    res["data"] = data
                    res["msg"] = "No today's booking found"
            except Exception as e:   
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Booking")

        elif self.arg == "future":
            try:
                join_b_sb = outerjoin(booking, sub_booking, booking.c.bookingID == sub_booking.c.bookingID)
                stmt = select([booking]).select_from(join_b_sb).where(sub_booking.c.date_today > cd)
                data = [dict(zip(r.keys(), r)) for r in conn.execute(stmt).fetchall()]
                if len(data) > 0:
                    res["code"] = "200"
                    res["data"] = data
                    res["msg"] = "ok"
                else:
                    res["code"] = "203"
                    res["data"] = data
                    res["msg"] = "No Future booking found"
            except Exception as e:   
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Booking")

        else:
            try:
                booking_list = select([booking]).distinct().where(booking.c.status==1)
                data = [dict(zip(r.keys(), r)) for r in conn.execute(booking_list).fetchall()]

                if len(data) == 0:
                    res["code"] = "204"
                    res["data"] = data
                    res["msg"] = "No book active found!"
                else:
                    res["code"] = "200"
                    res["data"] = data
                    res["msg"] = "ok"
                    
            except Exception as e:   
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Booking")

        return res


    def getBookingInactiveList(self):
        res = {}
        try:
            booking_list = select([booking]).where(booking.c.status==0)
            data = [dict(zip(r.keys(), r)) for r in conn.execute(booking_list).fetchall()]
            if len(data) == 0:
                res["code"] = "204"
                res["data"] = []
                res["msg"] = "No book inactive found!"
            else:
                res["code"] = "200"
                res["data"] = data
                res["msg"] = "ok"
                
        except Exception as e:   
            res["code"] = "203"
            res['data'] = []
            res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Booking")

        return res


    def deactivateBooking(self):
        res = {}

        try:
            check_status = select([booking]).where(booking.c.bookingID== self.queid).where(booking.c.status==0)
            res_check = conn.execute(check_status)
            if res_check.rowcount == 1:
                res["code"] = "202"
                res["id"] = self.queid 
                res["msg"] = "already deactivated"
                
            else:
                deactivate_booking = booking.update().where(booking.c.bookingID== self.queid).values(status=0)
                res_deactivate = conn.execute(deactivate_booking)

                res["code"] = "200"
                res["id"] = self.queid
                res["msg"] = "Successfully deactivated"
        except Exception as e:
            res["code"] = "204"
            res["id"] = self.queid
            res["msg"] = "Unable to deactivate"
        return res


    
    def activateBooking(self):
        res = {}
        try:
            check_status = select([booking]).where(booking.c.bookingID== self.queid).where(booking.c.status==1)
            res_check = conn.execute(check_status)
            if res_check.rowcount == 1:
                res["code"] = "202"
                res["id"] = self.queid 
                res["msg"] = "already activated"
                
            else:
                deactivate_booking = booking.update().where(booking.c.bookingID== self.queid).values(status=1)
                res_deactivate = conn.execute(deactivate_booking)

                res["code"] = "200"
                res["id"] = self.queid
                res["msg"] = "Successfully activate"
        except Exception as e:
            res["code"] = "204"
            res["id"] = self.queid 
            res["msg"] = "Unable to activate"
        return res


    def blockBookingDate(self):
        res = {}
        self.detail = {}
        self.detail = self.arg
        time  = check_time(self.arg["start_date"], self.arg["end_date"])
        self.detail["status"] = 1
        self.detail["time_consume"] = time
        
        try:
            check_block_head = select([block_head]).where(block_head.c.vehicleID==self.detail["vehicleID"])
            res_check_block_head = conn.execute(check_block_head)
            res_bh = conn.execute(check_block_head).fetchall()
            
            if res_check_block_head.rowcount >= 1:
                res_block_head = chck_block_head(res_bh, self.detail["start_date"] , self.detail["end_date"])
                if res_block_head > 0:
                    res["code"] = "203"
                    res["msg"] = "not available this date"
                else:
                    save_block = block_head.insert().values(self.detail) 
                    res_save = conn.execute(save_block)
                    res["code"] = "203"
                    res["data"] = res_save.inserted_primary_key
                    res["msg"] = "Successfully create booking "
                    
            else:
                save_block = block_head.insert().values(self.detail) 
                res_save = conn.execute(save_block)

                res["code"] = "203"
                res["data"] = res_save.inserted_primary_key
                res["msg"] = "Successfully create booking "
                
        except Exception as e:
                res["code"] = "203"
                res['data'] = []
                res['msg'] = "DB-LOG:{db_name} - {e}".format(e=e,db_name="Booking")

        return res



def hash_code():
    
    rnum = random.randint(1111,9999)
    t = time.strftime("%H%M%s")
    code = 'B{t}{rnum}'.format(t=t, rnum=rnum)
    rndcode = "{code}".format(code = code)

    return rndcode


def check_time(start_date, end_date):


    fmt = '%Y-%m-%d %H:%M:%S'
    tstamp1 = datetime.strptime(start_date, fmt)
    tstamp2 = datetime.strptime(end_date, fmt)
    
    tt = tstamp2 - tstamp1
    print("awdwaawdaw",tt)
    print("awd",tt.total_seconds())
    time_consume = tt.total_seconds()

    return time_consume


def insert_booking(date_today, detail, block):
    book_id = None
    sb = {}
   
    nbooking = booking.insert().values(detail)
    res_new = conn.execute(nbooking)
    book_id = res_new.inserted_primary_key

    block["bookingID"] = book_id
    nblock_head = block_head.insert().values(block)
    res_new_block_head = conn.execute(nblock_head) 

    for d_today in date_today:
         
        sb["date_today"] = d_today
        sb["bookingID"] = book_id
        ins_sub_bopoking = sub_booking.insert(sb)
        res_sub_booking = conn.execute(ins_sub_bopoking)


    return book_id




def chck_block_head(bh, start_date, end_date):
    start = datetime.strptime(start_date,'%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_date,'%Y-%m-%d %H:%M:%S')
    res = 0    
    for o in bh:
        if start < o["start_date"] and end < o['start_date']:
            # print("\n\n1 - pwede\n")
            res = 0 
        elif start > o["end_date"] and end > o['end_date']:
            # print("\n\n2 - pwede \n")
            res = 0 
        else:
            # print("\n\n3 - dili\n")
            res = res + 1 
    return res

# def deleteBooking(j,q):
#     res = {}
#     try:

#         chck_booking = select([booking]).where(booking.c.booking_id==q)
#         res_chck = conn.execute(chck_booking)

#         if res_chck.rowcount ==1:
#             delete_booking = booking.delete().where(booking.c.booking_id==q)
#             res_delete = conn.execute(delete_booking)
#             res["code"] = "200"
#             res["booking_id"] = q 
#             res["msg"] = "Successfully deleted"
#         else:
#             res['code'] = "203"
#             res["booking_id"] = q 
#             res["msg"] = "Invalid client id"
        
#     except Exception as e:
#         res['code'] = "400"
#         res['msg'] = "Bad request"
#     return res