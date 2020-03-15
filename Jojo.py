from datetime import *

class Jojo:

    def __init__(self, name=None, height=0, weight=0, date =None, stand_name = None, power = None, ):
        self.name = name
        self.height = height
        self.weight = weight
        self.date = date
        self.stand_name = stand_name
        self.power = power

    def show(self):
        return "Name: " + str(self.name) + " Height: " + str(self.height) + " Weight: " + str(self.weight) \
               + " Date: " + str(self.date)

    def add(self):
        self.name = input("Name: ")
        self.height = int(input("Height: "))
        self.weight = int(input("Weight: "))
        year = int(input("Year of birth: "))
        month = int(input("Month of birth: "))
        day = int(input("Day of birth: "))
        self.date = datetime(year, month, day)
        self.stand_name = input("Stand name: ")
        self.power = input("Special power: ")
        return "Name: " + str(self.name) + " Height: " + str(self.height) + " Weight: " + str(self.weight) \
               + " Date: " + str(self.date) + " Stand name: " + str(self.stand_name) \
               + " Special power: " + str(self.power)

    def show_stand(self):
        return "Name: " + str(self.name) +  " Stand name: " + str(self.stand_name) \
               + " Special power: " + str(self.power)



