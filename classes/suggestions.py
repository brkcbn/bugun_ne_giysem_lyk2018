class Suggestions():
    temperature = None
    precipitation = None
    def __init__(self, precipitation, temperature):
        self.temperature = temperature
        self.precipitation = precipitation
        clothe_too_cold = ["scarf", "glove", "thermals", "boot"]
        clothe_cold = ["scarf", "cap" "umbrella" ]
        clothe_normal = ["rain boots", "umbrella" ]
        clothe_hot = [ "sunglasses" , "light clothes"]
        clothe_too_hot = ["hat", "flip-flops", "sun glasses", "light clothes"]

        if precipitation is True :

            if precipitation == "Extreme":
                print("Take your {}, {}; wear your {} and {}.".format(clothe_too_cold))

            if precipitation == "Snow" :
                    pass

            if precipitation == "Rain" :
                    pass


            else:
                print("There is no precipitation")

        Extreme
        if self.temperature.isnumeric:
            self.temperature = int(self.temperature)
            if self.temperature <= 0 :
                pass
            elif self.temperature > 0 and self.temperature <= 13:
                pass
            elif self.temperature > 13 and self.temperature <= 24:
                pass
            elif self.temperature > 24 and self.temperature <= 35:Extreme
                pass
            elif self.temperature > 35:
                pass

        else:
            print("Temperature variable has not numeric value !")

sd = Suggestions("Extreme",24)
