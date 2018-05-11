from sqlalchemy import Table, Column, Integer, String, Float, MetaData, ForeignKey,func, select, outerjoin, case, literal_column
from sqlalchemy.sql import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import SESSION_OPTS
import sqlalchemy
import json
import datetime

# engine = sqlalchemy.create_engine('mysql://root:1..@127.0.0.1:3306/eagle1') # connect to server
engine = create_engine(SESSION_OPTS['session.url'], pool_size=40, max_overflow=-1, pool_recycle=3600, echo=True)

metadata = MetaData()
usrrole = Table('usr_role', 
        metadata,
        Column('id', Integer, primary_key=True),
        Column('role_name', String),
        Column('role_code', Integer),
        Column('role_status',Integer))

usrTable = Table('usr',
        metadata,
        Column('usrid', Integer,primary_key=True),
        Column('username', String),
        Column('pwd', String),
        Column('reg_date', String),
        Column('usr_status', String))
usrProfile = Table('userprofile',
                metadata,
                Column('usrpid', Integer,primary_key=True),
                Column('usrid', Integer),
                Column('firstname', String),
                Column('lastname', String),
                Column('email', String),
                Column('contact', String),
                Column('usrp_status', Integer),
                Column('created', Integer))
userpermit = Table('userpermit',
                metadata,
                Column('usrper_id', Integer,primary_key=True),
                Column('permit_val', Integer),
                Column('permit_status', Integer),
                Column('userid', Integer))


#quotation
qtheader = Table('qtheader',
        metadata,
        Column('qt_id', Integer,primary_key=True),
        Column('reg_date', String),
        Column('date_req', String),
        Column('clientid', String),
        Column('amt', Float),
        Column('vendorid',Integer),
        Column('booking_id', Integer),
        Column('particulars',String),
        Column('pointA_lat',String),
        Column('pointA_lon',String),
        Column('pointB_lat',String),
        Column('pointB_lon',String),
        Column('stat',Integer))

qtdetail = Table('qtdetail',
                metadata,
                Column('qtd_id', Integer, primary_key=True),
                Column('qth_id',Integer),
                Column('descrp',String),
                Column('qty',Integer),
                Column('price',Float),
                Column('type', Integer),
                Column('vendorid',Integer),
                Column('total',Float),
                Column('stat',Integer))

ven = Table('vendor',
        metadata,
        Column('ven_id', Integer, primary_key=True),
        Column('fname', String),
        Column('lanme', String),
        Column('address',String),
        Column('mobile', String),
        Column('tel', String),
        Column('email', String),
        Column('payment',String),
        Column('status', Integer),
        Column('CompanyName', String))
vehcle = Table('vehicle',
        metadata,
        Column('vehicle_id', Integer, primary_key=True),
        Column('vendor_id', Integer),
        Column('vechicle_type', String),
        Column('qty', Integer),
        Column('price',Float),
        Column('description', String),
        Column('platenumber', String),
        Column('stockonhand', Integer),
        Column('imgcount', Integer),
        Column('reg_date', String),
        Column('capacity', Float),
        Column('tankcapacity', Float),
        Column('unit', String),
        Column('reason_deactivation', String),
        Column('req_deactivate', Integer),
        Column('status', Integer)
        )



#client

client = Table('client',
        metadata,
        Column('client_id', Integer, primary_key=True),
        Column('client_type', Integer),
        Column('username', String),
        Column('password', String),
        Column('fname', String),
        Column('lname', String),
        Column('contact', Integer),
        Column('email', String),
        Column('address', String),
        Column('status', Integer)
        )



#Booking

booking = Table('booking',
        metadata,
        Column('bookingID', Integer, primary_key=True ),
        Column('vehicleID',Integer ),
        Column('client_id',Integer ),
        Column('start_date', String),
        Column('end_date', String),
        Column('picking_time', String),
        Column('pointA', String),
        Column('pointB', String),
        Column('price', Integer),
        Column('wDriver', Integer),
        Column('status', Integer),
        Column('booking_code', String)
        # Column('date_today', String)
        
        
        )

#Booking_date_blocking

block_head = Table('block_head',
                        metadata,
                        Column('blockID', Integer, primary_key=True ),
                        Column('bookingID',Integer ),
                        Column('start_date',String ),
                        Column('end_date', String),
                        Column('status', Integer),
                        Column('time_consume', Integer),
                        Column('vehicleID', Integer)
                        
)

sub_booking = Table('sub_booking',
                        metadata,
                        Column('id', Integer, primary_key=True),
                        Column('bookingID', Integer),
                        Column('date_today', String)
)
rating = Table('rating',
        metadata,
        Column('rating_id', Integer, primary_key=True),
        Column('vendor_id', Integer),
        Column('vehicle_id', Integer),
        Column('rate', Integer))
review = Table('review',
               metadata,
               Column('review_id', Integer, primary_key=True),
               Column('vendor_id', Integer),
               Column('vehicle_id', Integer),
               Column('reviews', Integer))


Session = sessionmaker(bind=engine)
conn = engine.connect()
session = Session(bind=conn)

# s = select([func.to_char(usr.reg_date,'%Y-%m-%d %H:%M')])
