import urllib.request
import json

API_KEY = "bd75792caa9b8949fbd39524fe8d0cc4"

city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        print("\nWeather Information")
        print("-------------------")
        print("City:", city)
        print("Temperature:", temp, "°C")
        print("Weather:", weather)

    else:
        print("City not found")

except:
    print("Error fetching data")
