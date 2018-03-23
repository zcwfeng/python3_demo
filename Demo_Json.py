import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

jsonStr = json.dumps(data)
print(jsonStr)
print(json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': ')))
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
text = json.loads(jsonData)
print(text)

#Demo Demjson
import demjson
dataDem = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
jsonStrDem = demjson.encode(dataDem)
print(jsonStrDem)
textDem = demjson.decode(jsonStrDem)
print(textDem)

# Demo 1
# import json
# data='''
# {
# "name":"Chuck",
# "phone":
# {
# "type":"intl",
# "number":"+1231231234"
# },
# "email":
# {
# "hide":"yes"
# }
# }'''
# info =json.loads(data)
# print('Name:',info["name"])
# print('Hide:',info["email"]["hide"])
