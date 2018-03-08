import json
data='''
{
"name":"Chuck",
"phone":
{
"type":"intl",
"number":"+1231231234"
},
"email":
{
"hide":"yes"
}
}'''
info =json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])
