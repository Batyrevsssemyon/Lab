class Player:

    def __init__(self, name=None, position=None, school=None):
        self.name = name
        self.position = position
        self.school = school

    def show(self):
        return "Name: " + str(self.name) + " Position: " + str(self.position) + " School: " + str(self.school)

    def add(self):
        self.name = input("Name: ")
        self.position = input("Position: ")
        self.school = input("School: ")
        return "Name: " + str(self.name) + " Position: " + str(self.position) + " School: " + str(self.school)