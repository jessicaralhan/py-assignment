import requests
import csv
import os
from datetime import datetime

city_name = input("enter city name : ")
app_key = os.getenv("APP_KEY")

if not app_key:
    print("Error: API key not found.")
    exit()

url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={app_key}"  
response = requests.get(url).json()
print(response)

if not response:
    print("city not found")
    exit()

city_name = response[0]["name"]
lat = response[0]["lat"]
lon = response[0]["lon"]

weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={app_key}&units=metric"
weather_response = requests.get(weather_url).json()
print(weather_response)

if "weather" not in weather_response or not weather_response["weather"]:
    print("Error: Weather data not found.")
    exit()

print(f"weather in {city_name} : condition : {weather_response['weather'][0]['description']},  temperature: {weather_response['main']['temp']}°C , humidity : {weather_response['main']['humidity']}")

condition = weather_response['weather'][0]['description']
humidity = weather_response['main']['humidity']
temperature = weather_response['main']['temp']
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

file_exists = os.path.exists("file.csv")

with open("file.csv", "a", newline='') as newfile:
    writer = csv.writer(newfile)
    if not file_exists or os.stat("file.csv").st_size == 0:  # Add header only if file is empty
        writer.writerow(["Date", "City Name", "Condition", "Temperature", "Humidity"])
    writer.writerow([date, city_name, condition, temperature, humidity])  

with open("second_file.txt", "a") as txtfile:
    txtfile.write(f"\nDate: {date}\n")
    txtfile.write(f"City: {city_name}\n")
    txtfile.write(f"Condition: {condition}\n")
    txtfile.write(f"Humidity: {humidity}\n")
    txtfile.write(f"Temperature: {temperature}°C\n")

# import requests
# import csv
# import os
# from datetime import datetime


# city_name = input("enter city name : ")
# app_key = os.getenv("APP_KEY")
# # app key has to be hidden get it as an environment variable 
# # app key which is created manually on open weather map api is the app id

# url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={app_key}"  
# response = requests.get(url).json()
# print(response)
# # check if the city name matches the response name https://api.openweathermap.org/geo/1.0/direct?q=dl&limit=1&appid=f7070b66bd36bc6ddb770ab210408a10 
# # where this url gives a diffrenet response 

# if not response:   
#     print("city not found")
#     exit()

# city_name = response[0]["name"]
# lat = response[0]["lat"]
# lon = response[0]["lon"]

# weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={app_key}" 
# weather_response = requests.get(weather_url).json()
# print(weather_response)
# # check if the weather list in weather response is not empty
# if "weather" not in weather_response:
#     print("Error: Weather data not found.")
#     exit()
#     print(f"weather in {city_name} : condition : {weather_response['weather'][0]['description']},  temperature: {weather_response['main']['temp']}°C , humidity : {weather_response['main']['humidity']}")
    
#     condition = weather_response['weather'][0]['description']
#     humdity = weather_response['main']['humidity']
#     temperature = weather_response['main']['temp']
#     date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open("file.csv", "a", newline='') as newfile:
#         writer = csv.writer(newfile)
#         writer.writerow(["Date", "City Name", "Condition", "Temperature", "Humidity"])
#         writer.writerow([date, city_name, weather_response['weather'][0]['description'], weather_response['main']['temp'], weather_response['main']['humidity']])  
# # add date 

    

#     with open("second_file.txt", "a") as txtfile:
#         txtfile.write(f"condition : {condition}\n")
#         txtfile.write(f"humidity : {humdity}\n")
#         txtfile.write(f"temperature : {temperature}\n")

    