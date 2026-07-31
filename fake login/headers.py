import requests

url = "https://httpbin.org/headers"

headers = {
    "name": "Yassin",
"country": "Egypt",
"job": "AI Automation Engineer"
}

response = requests.get(url, headers=headers)

print(response.json())