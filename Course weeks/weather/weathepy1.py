import requests

api_key = "87a478799946582566e1eebe9804d7ea"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url = base_url+ "appid="  + api_key + "&q=" +city_name
response = requests.get(complete_url)
x=response.json()
visibility = x['visibility']
weather = x['weather'][0]['description']
timezone = x['timezone']
temp = x["main"]["temp"]-273
humidity = x["main"]["humidity"]


print("weather:",str(weather,),"\n",
"visibility:",str(visibility)+"m","\n",
"timezone:",str(timezone)+"hours","\n",
"temp:",str(temp)+"°","\n",
"humidity:",str(humidity)+"percent","\n")


