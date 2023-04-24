import requests
import json
import jsonpath
import pytest

# Api URL
url= "https://reqres.in/api/users/"


def test_newuser():
    file = open('C:\\Users\\gulsah\\Desktop\\APİ\\CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201

def test_otheruser():
    file = open('C:\\Users\\gulsah\\Desktop\\APİ\\CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    Id = jsonpath.jsonpath(response_json, 'id')
    print(Id[0])

