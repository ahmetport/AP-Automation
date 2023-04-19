import requests
import json
import jsonpath

# Api URL
url= "https://reqres.in/api/users/ "

#Read Input Json File
file=open('C:\\Users\\gulsah\\Desktop\\APİ\\CreateUser.json','r')
json_input=file.read()
request_json=json.loads(json_input)
print(request_json) #{'name': 'autodidactic', 'job': 'tester'}

#Make Post Request with json input body
response=requests.post(url,request_json)
print(response.content)

#Validating Response Code
assert response.status_code == 201

# Fetch Header from response
print(response.headers.get('Content-Length'))

#Parse Response To Json Format
response_json=json.loads(response.text)

#Pick ID Using Json Path
Id=jsonpath.jsonpath(response_json,'id')
print(Id[0])

