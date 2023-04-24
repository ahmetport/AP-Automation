import requests
import json
import jsonpath

# Api URL
url= "https://reqres.in/api/users/?page=2 "

# Send Get Request
response=requests.get(url) # <Response [200]>
print(response)

#Display Response Content
#print(response.content)
#print(response.headers)

#Parse Response JsonFormat
json_response=json.loads(response.text)
#print(json_response)

#fetch value using jsonpath
pages=jsonpath.jsonpath(json_response,"total_pages")
#print(pages[0]) # 2
assert pages[0]== 2 #verify



