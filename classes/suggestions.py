class Suggestions():
    temperature = None
    precipitation = None
    def __init__(self, precipitation, temperature):
        self.temperature = temperature
        self.precipitation = precipitation
        clothe_too_cold = ["cap", "scarf", "glove", "thermals", "boot"]
        clothe_cold = ["scarf", "cap" "umbrella" ]
        clothe_normal = ["rain boots", "umbrella" ]
        clothe_hot = [ "sunglasses" , "light clothes"]
        clothe_too_hot = ["hat", "flip-flops", "sun glasses", "light clothes"]

        if precipitation is True :
            if precipitation == "Snowy" :
                pass
            
            else :
                pass
        else:
            print("There is no precipitation")


        if self.temperature.isnumeric:
            self.temperature = int(self.temperature)
            if self.temperature <= 0 :
                pass
            elif self.temperature > 0 and self.temperature <= 13:
                pass
            elif self.temperature > 13 and self.temperature <= 24:
                pass
            elif self.temperature > 24 and self.temperature <= 35:
                pass
            elif self.temperature > 35:
                pass

        else:
            print("Temperature variable has not numeric value !")

        