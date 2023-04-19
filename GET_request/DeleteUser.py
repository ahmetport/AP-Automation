import requests

# Api URL
url= "https://reqres.in/api/users/2 "

#delete response

response= requests.delete(url)
print(response)

#fetch response code  // yanıt kodunu getir
print(response.status_code)
assert response.status_code==204