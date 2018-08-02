import json
import requests

class Weather():
    coordinates=""
    city_name=""
    api_key=""
    data=""
    def __init__(self,api_key):
        self.api_key = api_key  
    

    def get_forecast_by_name(self,city_name):
        #get data from API with city name
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q={city},tr&appid={key}".format(city=city_name,key=self.api_key))
        #parse json
        data=data.json()
        
        return data 
    
    def get_forecast_by_coordinates(self,coordinates):
       #self.coordinates=coordinates
        latitude=coordinates.get("latitude")
        longitude = coordinates.get("longitude")
       
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={key}".format(lat=latitude,long=longitude,key=self.api_key))
        data=data.json()
        return data
        
    
    
    
##weather = Weather("92bb6add0822613f2ca9dd20116528a8")    
##city_data=weather.get_forecast_by_coordinates({'latitude': 40.6344, 'longitude': 31.6725})
##print(city_data)
##        
    