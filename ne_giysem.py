import logging
import socket
from classes.coordinates import Coordinates
from classes.weather import Weather
from classes.suggestions import Suggestions


class NeGiysem():
    weather_api_key="92bb6add0822613f2ca9dd20116528a8"
    coordinates_api_key="a5966744b2c34ab0d19f2cf74c440dd6"
    
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


    
    