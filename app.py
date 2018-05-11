from flask import *
from config import IPHOST
from routes.userroutes.userroutes import userapi
from routes.vendor.vendorroutes import vendorapi
from routes.vehicle.vehicle import vehicleapi
from routes.bookingroutes.booking import *
from routes.clientroutes.client import *
# from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
# from routes.social_auths_routes.social_media_auths import *



app = Flask(__name__)

# app.config['SECRET_KEY'] = 'thisissupposetobeasecret'

# twitter_blueprint = make_twitter_blueprint(api_key='rgFxAd5wAQtkRt0S2PnMMi0nv', api_secret='MvrCpz21roYXWOROBeMcMktE4yAJOhBtr2Aqtiloiqze3gylNu')

# app.register_blueprint(twitter_blueprint, url_prefix='/twitter_login')

# app.register_blueprint(social_media_auths)

app.register_blueprint(userapi)
app.register_blueprint(vendorapi)
app.register_blueprint(vehicleapi)
app.register_blueprint(bookingapi)
app.register_blueprint(clientapi)






if (__name__ == "__main__"):
    app.debug = True
    app.run(host=IPHOST['IP'], port = IPHOST['PORT'])
