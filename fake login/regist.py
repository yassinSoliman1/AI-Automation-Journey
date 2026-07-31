import requests

url = "https://httpbin.org/post"

print("========= Register =========")
name = input('Name: ')
email = input('Emaill: ')
age = input('Age: ')
password = input('password: ')

data ={
    "name": name ,
    "email" : email ,
    "age" : age,
    "password": password
}

response = requests.post(url, json=data)
result = response.json()
print(result)

    
    