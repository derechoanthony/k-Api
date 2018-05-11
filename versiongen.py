import jwt
import json
var = raw_input("Please enter version Number: ")
d = {}
d['ver'] = "v{input}.0".format(input=str(var))
d['author'] = 'Mr.T'

encrypt = jwt.encode(d, 'secret', algorithm='HS256')
file = open("curver.log","w")
file.write(encrypt)
print "version control:{v}\ncode:{e}".format(v=var,e=encrypt)
print(d)
# def is_json(myjson):
#   try:
#     json_object = json.loads(myjson)
#   except ValueError, e:
#     return False
#   return True


# print jwt.encode(x, 'secret', algorithm='HS256')
# print str(var)
