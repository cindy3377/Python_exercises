
import requests
import json
from requests import Response

#part1

response = requests.get(url="https://api.chucknorris.io/jokes/random")
response.raise_for_status()

data = response.json()
joke = data["value"]

print(joke)


#part2
municipality = input("Enter a municipality: ")

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?units=metric&q=" + municipality + "&appid=9794d417550c88cdee38f3a6a544a002")
response.raise_for_status()

data = response.json()
weather = data["weather"][0]["description"]
temp_in_celsius = int(data["main"]["temp"])

print(f"The current weather is", weather)
print(f"The current temperature is", temp_in_celsius, "degree Celcius")

