class Suggestions():
    temperature = None
    precipitation = None

    def __init__(self, precipitation, temperature):
        self.temperature = temperature
        self.precipitation = precipitation
        clothe_too_cold = ["scarf", "glove", "thermals", "boot"]
        clothe_cold = ["scarf", "cap","umbrella"]
        clothe_rain = ["rain boots", "umbrella"]
        clothe_hot = ["sunglasses", "light clothes"]
        clothe_too_hot = ["hat", "flip-flops", "sun glasses", "light clothes"]

        if precipitation:

            if precipitation == "Extreme":
                print("Take your {} and {}, wear your {} and {}.".format(*clothe_too_cold))

            elif precipitation == "Snow":
                print("Wear your {} and {}, do not forget to take an {}.".format(*clothe_cold))

            elif precipitation == "Rain":
                print("Wear your {}, do not forget to take an {}.".format(*clothe_rain))


        else:
            print("There is no precipitation")


        if self.temperature.isnumeric:
            self.temperature = int(self.temperature)

            if self.temperature <= 0:
                print("Be careful while driving or walking!")

            elif self.temperature > 0 and self.temperature <= 13:
                print("Spring is coming")

            elif self.temperature > 13 and self.temperature <= 24:
                print("Mont Beni")

            elif self.temperature > 24 and self.temperature <= 35:
                print("Yaz geldi, her gece sokakta")

            elif self.temperature > 35:
                print("Esmiyooor!")

        else:
            print("Temperature variable is not a string and has not a numeric value !")


sd = Suggestions("Snow", "-5")
