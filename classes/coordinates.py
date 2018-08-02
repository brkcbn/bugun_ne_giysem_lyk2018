import requests

class Coordinates():
    latitude = ""
    longitude = ""
    ip = None
    #ex{'latitude': 40.6344, 'longitude': 31.6725}
    coordinate={}
    access_key=None
    def __init__(self,access_key):
        requests_data= requests.get(r'http://jsonip.com')
        self.ip=requests_data.json()['ip']
        self.access_key=access_key
        
    def give_my_coordinates(self):
        try:
            all_data = requests.get("http://api.ipstack.com/{ip}?access_key={access_key}".format(ip= self.ip,access_key= self.access_key)).json()
            self.latitude = all_data['latitude']
            self.longitude = all_data['longitude']
            self.coordinate= {"latitude": self.latitude,"longitude":self.longitude}
            return self.coordinate
        except Exception as e:
            print(e)
            return False
