import requests
import json
import jsonpath

def test_add_new_data():
    App_url="https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/gulsah/Desktop/APİ/App_data.json', 'r')
    request_json=json.loads(f.read())
    response=requests.post(App_url,request_json)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    test_techurl="https://thetestingworldapi.com/api/technicalskills"
    f=open('C:/Users/gulsah/Desktop/APİ/Techurlskills.json', 'r')
    request_json = json.loads(f.read())
    request_json['id']=int(id[0])
    request_json['st_id']=id[0]
    response = requests.post(test_techurl, request_json)
    print(response.text)

    test_Adresss = "https://thetestingworldapi.com/api/addresses"
    f = open('C:/Users/gulsah/Desktop/APİ/Adresss.json', 'r')
    request_json = json.loads(f.read())
    request_json['stId']=id[0]
    response = requests.post(test_Adresss, request_json)

    finally_idurl="https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response=requests.get(finally_idurl)
    print(response.text)



