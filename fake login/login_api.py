import requests

url = "https://httpbin.org/post"

username = input("Enter username: ")
password = input("Enter password: ")

data = {
    "username":username ,
    "password": password
}
response = requests.post(url, json=data)
result = response.json()
print(result)