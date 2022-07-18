class Vehicle:
    def __init__(self, make, yrmodel):
        self.__make = make
        self.__yrmodel = yrmodel

    def getmake(self):
        return self.__make

    def getyrmodel(self):
        return self.__yrmodel

class Car(Vehicle): #establishing inheritance by having parent class inside ()
    def __init__(self, make, yrmodel, doors):
        Vehicle.__init__(self, make, yrmodel)
        self.__doors = doors
    
    def getdoors(self):
        return self.__doors

