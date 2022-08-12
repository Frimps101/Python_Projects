#! python3
# open_local_weather.py - A simple python program to open the browser to the URL of your local weather
# weather url: https://www.accuweather.com/en/gh/accra/178551/weather-forecast/178551

import webbrowser
import sys

if len(sys.argv) > 1:
    weather_url = sys.argv[1]
    # print(weather_url)
    webbrowser.open(weather_url)
