dictionary = {'coord': {'lon': -0.1257, 'lat': 51.5085},
     'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
     'base': 'stations', 'main': {'temp': 300.36, 'feels_like': 300.34, 'temp_min': 298.15, 'temp_max': 302.79, 'pressure': 1032, 'humidity': 43},
     'visibility': 10000, 'wind': {'speed': 4.12, 'deg': 280},
     'clouds': {'all': 6}, 'dt': 1657286482, 'sys': {'type': 2, 'id': 268730, 'country': 'GB', 'sunrise': 1657252385, 'sunset': 1657311456},
     'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}

#print(dictionary['main']['humidity'])


condiitons  = dictionary['weather'][0]['description']

curr_temp = int(dictionary['main']['temp'] - 273.15)

humidity = dictionary['main']['humidity']

sun_emoji = "\U0001F31E"

print("Conditions:",condiitons,sun_emoji+"\n",
      "Temprature:",str(curr_temp)+"°","\n",
      "Humidity:",str(humidity)+"%")


