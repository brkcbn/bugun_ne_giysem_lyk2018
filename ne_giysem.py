import logging
import socket
from classes.coordinates import Coordinates
from classes.weather import Weather
from classes.suggestions import Suggestions


class NeGiysem():
    weather_api_key="92bb6add0822613f2ca9dd20116528a8"
    coordinates_api_key="a5966744b2c34ab0d19f2cf74c440dd6"
    city=""
    coordinates=""
    
    def __init__(self):
        pass
       
    #get coordinates
    def get_coordinates(self,coordinates_api_key):
        coordinates =Coordinates(coordinates_api_key)
        coordinates = coordinates.give_my_coordinates()
        if coordinates:
           return coordinates
        else:
           get_city_name()
    
    
    #ask city name
    def get_city_name(self):
        city=input("Please enter the city name for weather forecast")
        self.city=city
      
    
    #get weather forecast
    def get_weather_forecast(self,coordinates=None):
        weather = Weather(self.weather_api_key)
        self.coordinates=coordinates
        if self.coordinates:
            return weather.get_forecast_by_coordinates(self.coordinates)
        else:
            return weather.get_forecast_by_name(self.city)
           
        

    def get_suggestions(self,degrees,precipitation):
        suggestions = Suggestions(degrees,precipitation)
        return suggestions

    
app = NeGiysem()
#get coordinates
coordinates = app.get_coordinates(app.coordinates_api_key)

#get weather forecast
data=app.get_weather_forecast(coordinates)
suggestion = Suggestions("Extreme","-5")
#get weather main
suggestion.create()

#get temp
#minus 273.15
#get suggestions

