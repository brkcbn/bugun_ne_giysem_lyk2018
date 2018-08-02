import requests
import json
class Coordinates():
    latitude = ""
    longitude = ""
    ip = None
    def find_ip(self):
        r = requests.get(r'http://jsonip.com')
        self.ip = r.json()['ip']
        print('Your IP is', self.ip)
    def give_my_coordinates(self):
        ham_data = requests.get("http://api.ipstack.com/{}?access_key=a5966744b2c34ab0d19f2cf74c440dd6".format(self.ip)).json()
        print(ham_data)

        self.latitude = ham_data['latitude']
        self.longitude = ham_data['longitude']
        return self.latitude , self.longitude


api = Coordinates()
api.find_ip()
api.give_my_coordinates()

