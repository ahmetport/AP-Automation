import requests
import json
import jsonpath

# Api URL
url= "https://reqres.in/api/users/2"

#Read Input Json File
file=open('C:\\Users\\gulsah\\Desktop\\APİ\\CreateUser.json','r')
json_input=file.read()
request_json=json.loads(json_input)
print(request_json) #{'name': 'autodidactic uptadet', 'job': 'tester updated'}

#Make PUT request with json input body
response=requests.put(url,request_json)


#validating response code
assert response.status_code ==200

# Parse Response Content
response_json=json.loads(response.text)
uptadetList=jsonpath.jsonpath(response_json,'updatedAt')
print(uptadetList[0]) #2023-04-20T11:36:18.116Z