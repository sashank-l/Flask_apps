import requests


API_KEY = "your api key"

location = input("input your location: ")

r = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
)

print(r.text)


# you can see the response from the api like this -   {"coord":{"lon":88.3697,"lat":22.5697},
#            "weather":[{"id":721,"main":"Haze","description":"haze","icon":"50d"}],"base":"stations",
#             "main":{"temp":28.97,"feels_like":34.44,"temp_min":28.97,"temp_max":28.97,"pressure":1008,"humidity":79,
#             "sea_level":1008,"grnd_level":1007},"visibility":3500,"wind":{"speed":1.54,"deg":110},
#            "clouds":{"all":40},"dt":1729337506,"sys":{"type":1,"id":9114,"country":"IN","sunrise":1729296272,
#            "sunset":1729337885},"timezone":19800,"id":1275004,"name":"Kolkata","cod":200}
