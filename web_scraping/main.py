import requests
import csv

city_name = input("enter city name : ")

url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid=f7070b66bd36bc6ddb770ab210408a10"
response = requests.get(url).json()
print(response)
if response:
    lat = response[0]["lat"]
    lon = response[0]["lon"]

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=f7070b66bd36bc6ddb770ab210408a10"
    weather_response = requests.get(weather_url).json()
    print(f"weather in {city_name} : condition : {weather_response['weather'][0]['description']},  temperature: {weather_response['main']['temp']}°C , humidity : {weather_response['main']['humidity']}")

    with open("file.csv", "w", newline='') as newfile:
        writer = csv.writer(newfile)
        writer.writerow(["City Name", "Condition", "Temperature", "Humidity"])
        writer.writerow([city_name, weather_response['weather'][0]['description'], weather_response['main']['temp'], weather_response['main']['humidity']])  


    condition = weather_response['weather'][0]['description']
    humdity = weather_response['main']['humidity']
    temperature = weather_response['main']['temp']
    with open("second_file.txt", "a") as txtfile:
        txtfile.write(f"condition : {condition}\n")
        txtfile.write(f"humidity : {humdity}\n")
        txtfile.write(f"temperature : {temperature}\n")