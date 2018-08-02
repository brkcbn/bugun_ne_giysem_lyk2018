class Weather():
    coordinates=""
    city_name=""
    
    def __init__(self):
      pass
    

    def get_forecast_by_name(self,city_name):
        self.city_name = city_name
        return self.city_name
    
    def get_forecast_by_coordinates(self,coordinates):
        
        self.coordinates=coordinates
        return self.coordinates
    
    
        
        
        