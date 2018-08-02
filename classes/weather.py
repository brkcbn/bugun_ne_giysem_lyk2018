import json

class Weather():
    coordinates=""
    city_name=""
    api_key=""
    def __init__(self,api_key):
        self.api_key = api_key  
    

    def get_forecast_by_name(self,city_name):
        self.city_name = city_name
        return self.city_name
    
    def get_forecast_by_coordinates(self,coordinates):
        print("coordinate")
        self.coordinates=coordinates
        return self.coordinates
    
    def get_data():
        data = requests.get('https://v2.sg.media-imdb.com/suggests/{aramailk}/{arama}.json'.format(aramailk=kullanici_girdisi[0],arama=kullanici_girdisi))

    
    
    
        
        
    