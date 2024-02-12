import requests

lat = 56.944096
long = 24.109085

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m&timezone=auto")

data = response.json()

data = data['hourly']

time = data['time']

tempreature = data['temperature_2m']

print(len(time))
print(len(tempreature))
