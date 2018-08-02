import logging
import socket
from classes.coordinates import Coordinates
from classes.weather import Weather
from classes.suggestions import Suggestions


class NeGiysem():
    weather_api_key=""
    coordinates_api_key=""
    
    def __init__(self):
       print("test")
    
    
       
    #get coordinates
    def get_coordinates(coordinates_api_key):
        coordinates =Coordinates()
        if coordinates:
            return coordinates
        else:
            #get city
            self.get_city_name()
        
    
    #ask city name
    def get_city_name(self):
        city=input("Please enter the city name for weather forecast")
        return city
    
    #get weather forecast
    def get_weather_forecast():
        weather = Weather()
        pass

    def get_suggestions():
        pass


    
    