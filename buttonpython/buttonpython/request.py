import requests

data=requests.get("http://reqres.in/api/users")

print(data.text)
