import requests
import jwt
file = open("curver.log","r")
d = file.read()
decrypt = jwt.decode(d, verify=False)
ver = decrypt["ver"]