from pprint import pprint
import requests


API_KEY = 'abfd6b9844bc94c2c4fcf3d2f3cac767'

city = input('Enter a city: ')

URL = f'http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}'

data = requests.get(URL).json()

pprint(data)
