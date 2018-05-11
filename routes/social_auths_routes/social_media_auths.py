from module.controller.headerque import process_header
from module.controller.jwtGen import *
from flask import *
from flask import Blueprint
from routes.static import ver
import requests
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter





social_media_auths = Blueprint('social_media_auths', __name__)


@social_media_auths.route('/twitter')
def twitter_login():

    if not twitter.authorized:
        return redirect(url_for('twitter.login'))
    account_info = twitter.get('account/verify_credentials.json')
    for i in account_info:
        print(i)

    if account_info.ok:
        account_info_json = account_info.json()
        return 'Your twitter name is @{}'.format(account_info_json['screen_name'])
    return 'Request Failed'



