import json

class Weather():
    coordinates=""
    city_name=""
    api_key=""
    data=""
    def __init__(self,api_key):
        self.api_key = api_key  
    

    def get_forecast_by_name(self,city_name):
        data=self.get_data([self.city_name,""])
        return data 
    
    def get_forecast_by_coordinates(self,coordinates):
        print("coordinate")
        self.coordinates=coordinates
        data=self.get_data(["",coordinates])
        return data
        
    
    def get_data(self,*args):
        city=args[0]
        coordinates=args[1]
        data=""
        if city:
            data = requests.get("https://api.openweathermap.org/data/2.5/weather?q={city},tr&appid={key}").format(city=city,key=self.api_key)
        elif coordinates:
            #by coordinates
            data = requests.get("https://api.openweathermap.org/data/2.5/weather?q={city},tr&appid={key}").format(city=city,key=self.api_key)
            
       
        return data
    
    
    
    
        
        
    