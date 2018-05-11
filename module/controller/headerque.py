import requests
from flask import Flask, request, jsonify
from validator import * 
from module.model.user import *
from module.model.vendor import *
from module.model.vehicle import *
from module.model.booking import *
from module.model.client import *

from module.model.gis import *
from module.model.feedback import *


class headerAttr(object):
    def __init__(self,arg,q=None):
        self.header = request.headers['Authorization']
        self.json_input = request.json if type(request.json).__name__=='dict' else request.json
        self.x = getToken(self.header,[" "])
        self.data = {}
        self.q = q
        self.entry = arg
    def chkdata(self):
        if self.x["code"] == "200" and self.x["data"]["uid"] != "":
            """
                Module's 
            """
            #-User
            if self.entry == "_userEntryData":
                self.data = UserEntry(self.json_input,self.x["data"])
            elif self.entry == "_userNewAccess":
                self.data = userNewAccess(self.json_input,self.x["data"])
            elif self.entry == "_singleUserSearch":
                self.data = userSingleSearch(self.json_input,self.q)
            elif self.entry == "_usrlist":
                self.data = multipleSearch()
            elif self.entry == "_userEdit":
                self.data = userEdit(self.json_input)
            elif self.entry == "_userDel":
                self.data = userDel(self.json_input,self.q)
            elif self.entry =="_userrole":
                self.data = getUserRole()
            elif self.entry == "_appuseractivate":
                self.data = userActivate(self.json_input,self.q)
            #-vendor
            elif self.entry == "_vendorcreate":
                self.data = vendor.regVendor(vendor(self.json_input,self.x["data"]))   
            elif self.entry == "_vendorupdate":
                self.data = vendor.updateVendor(vendor(self.json_input,self.x["data"],self.q))
            elif self.entry == "_vendorlist":
                self.data = vendor.VendorList(vendor())
            elif self.entry == "_vendorlistsingle":
                self.data = vendor.SingleVendorList(vendor("","",self.q))
            elif self.entry == "_vendordeactivate":
                self.data = vendor.deactivatevendor(vendor(self.json_input))
            elif self.entry == "_vendoractivate":
                self.data = vendor.activatevendor(vendor(self.json_input))
            elif self.entry == "_vendorinactive":
                self.data = vendor.VendorListinactive(vendor())

            #-vehicle
            elif self.entry == "_vehiclecreate":
                self.data = vehicle.regVehicle(vehicle(self.json_input,self.x["data"]))
            elif self.entry == "_apisinglesearch":
                self.data = vehicle.vehiclesiglelist(vehicle('','',self.q))
            elif self.entry == "_vehicleupdate":
                self.data = vehicle.updateVehicle(vehicle(self.json_input,self.x["data"],self.q))
            elif self.entry == "_vehiclereqdeactivate":
                self.data = vehicle.reqDeactivate(vehicle(self.json_input,self.x['data']))
            elif self.entry == "_apivehiclelist":
                self.data = vehicle.vehiclelist(vehicle())
            elif self.entry == "_apivehicledeactivatelist":
                self.data = vehicle.vehicledeactivatelist(vehicle())
            elif self.entry == "_apivehicle_appDeactivate":
                self.data = vehicle.appDeactivate(vehicle(self.json_input))
            elif self.entry == "_apivehicle_activate":
                self.data = vehicle.activateVehicle(vehicle(self.json_input))



            #Client
            elif self.entry == "_clientEntry":
                # self.data = newCLientEntry(self.json_input,self.x["data"])
                self.data = clientApi.newCLientEntry(clientApi(self.json_input,self.x["data"]))


            elif self.entry == "_clientActiveList":
                # self.data = getClientActiveList()
                self.data = clientApi.getClientActiveList(clientApi())


            elif self.entry == "_clientInactiveList":
                # self.data = getClientInactiveList()
                self.data = clientApi.getClientInactiveList(clientApi())
                

            elif self.entry == "_clientUpdate":
                self.data = clientApi.updateClient(clientApi(self.json_input))   

            elif self.entry == "_clientDeactivate":
                self.data = clientApi.deactivateClient(clientApi("", "",self.q))

            elif self.entry == "_clientActivate":
                # self.data = activateClient(self.json_input,self.q)  
                self.data = clientApi.activateClient(clientApi("", "",self.q))
                
            elif self.entry == "_clientSearch":
                self.data = clientApi.singleSearch(clientApi("","",self.q))


            # elif self.entry == "_clientDelete":
            #     self.data = deleteClient(self.json_input,self.q)
            
            #Booking
            elif self.entry == "_bookingEntry":
                self.data = bookingApi.newBookingEntry(bookingApi(self.json_input,self.x["data"])) 
            elif self.entry == "_bookingUpdate":
                self.data = bookingApi.updateBooking(bookingApi(self.json_input,self.x["data"])) 
            elif self.entry == "_singleSearch":
                self.data = bookingApi.searchBooking(bookingApi("","",self.q))    


            elif self.entry == "_bookingActiveList":
                self.data = bookingApi.getBookingActiveList(bookingApi(self.q,"","")) 
                
            elif self.entry == "_bookingInactiveList":
                self.data = bookingApi.getBookingInactiveList(bookingApi()) 
            elif self.entry == "_bookingDeactivate":
                self.data = bookingApi.deactivateBooking(bookingApi("","",self.q))
            elif self.entry == "_bookingActivate":
                self.data = bookingApi.activateBooking(bookingApi("","",self.q))
            elif self.entry == "_bookingBlock":
                self.data =bookingApi.blockBookingDate(bookingApi(self.json_input))

            # elif self.entry == "_bookingDelete":
            #     self.data = deleteBooking(self.json_input,self.q)

                
            
            #-feedback
            #   > rating
            elif self.entry == "_apratings":
                self.data = feedback.ratingentry(feedback(self.json_input))
            elif self.entry == "_appallrating":
                self.data = feedback.allrating(feedback(self.q))
            elif self.entry == "apavehicle":
                self.data = feedback.vehiclerating(feedback(self.q))
            #  > review
            elif self.entry == "_appreviewsEntry":
                self.data = feedback.reviewsEntry(feedback(self.json_input))
            elif self.entry == "_apallreview":
                self.data = feedback.allreview(feedback(self.q))
            elif self.entry == "_apavehiclereview":
                self.data = feedback.vehiclereview(feedback(self.q))
            
                
            #-GIS
            elif self.entry == "_apiGis":
                print(self.q)
                self.data = GIS.getGis(GIS(self.q))

        elif self.x["data"]["uid"] == "":
            self.data["code"] = 203
            self.data["message"] = "Invalid Entry UID is null!"
        else:
            self.data["code"] = self.x["code"]
            self.data["message"] = self.x["msg"]
        return jsonify(self.data)

def process_header(d,q=None):
    h = headerAttr(d,q)
    res = headerAttr.chkdata(h)
    print(d)
    return res


def process_Frontend(typ):
    json_input  = request.json if type(request.json).__name__=='dict' else request.json
    data = {}
    if typ == '_vendorcreate':
        data = vendor.regVendor(vendor(json_input))
    return jsonify(data)

    