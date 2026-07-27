import requests

city = input("Enter city: ")
url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
response = requests.get(url)
data = response.json()
latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
weather_response = requests.get(weather_url) 
weather_data = weather_response.json()


print(f"City: {data["results"][0]["name"]}")
print(f'temperature: {weather_data["current"]["temperature_2m"]} °C')
print(f'humidity: {weather_data["current"]["relative_humidity_2m"]} %')
print(f'wind speed: {weather_data["current"]["wind_speed_10m"]} km/h')