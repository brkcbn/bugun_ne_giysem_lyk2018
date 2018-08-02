import requests
import json


class Coordinates():
    ip = None

    def find_ip(self):
        import socket
        self.ip = socket.gethostbyname(socket.gethostname())


api = Coordinates()
api.find_ip()
