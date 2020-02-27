import requests

# url = "https://api.getpostman.com/collections"
#
# payload = {}
# files = {}
# headers = {
#   'X-Api-Key': 'PMAK-5e578a489d0dd400293c20af-70a70569b705e02e4b410644a9b2b2e30a'
# }
#
# response = requests.request("GET", url, headers=headers, data = payload, files = files)
#
# print(response.text)



url = "https://api.getpostman.com/collections"

payload = "{\n  \"collection\": {\n    \"variables\": [],\n    \"info\": {\n      \"name\": \"Sample Collection\",\n      \"description\": \"This is just a sample collection.\",\n      \"schema\": \"https://schema.getpostman.com/json/collection/v2.0.0/collection.json\"\n    },\n    \"item\": [\n      {\n        \"name\": \"This is a folder\",\n        \"description\": \"\",\n        \"item\": [\n          {\n            \"name\": \"Sample POST Request\",\n            \"request\": {\n              \"url\": \"echo.getpostman.com/post\",\n              \"method\": \"POST\",\n              \"header\": [\n                {\n                  \"key\": \"Content-Type\",\n                  \"value\": \"application/json\",\n                  \"description\": \"\"\n                }\n              ],\n              \"body\": {\n                \"mode\": \"raw\",\n                \"raw\": \"{\\n\\t\\\"data\\\": \\\"123\\\"\\n}\"\n              },\n              \"description\": \"This is a sample POST Request\"\n            },\n            \"response\": []\n          }\n        ]\n      },\n      {\n        \"name\": \"Sample GET Request\",\n        \"request\": {\n          \"url\": \"echo.getpostman.com/get\",\n          \"method\": \"GET\",\n          \"header\": [],\n          \"body\": {\n            \"mode\": \"formdata\",\n            \"formdata\": []\n          },\n          \"description\": \"This is a sample GET Request\"\n        },\n        \"response\": []\n      }\n    ]\n  }\n}"
headers = {
  'X-Api-Key': 'PMAK-5e578a489d0dd400293c20af-70a70569b705e02e4b410644a9b2b2e30a',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))

print(response.text)

