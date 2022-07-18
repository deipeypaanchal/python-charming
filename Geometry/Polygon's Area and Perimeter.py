'''
****** N-sided Polygon class definition and main function ******
-> This program is designed to calculate the area and perimeter of a regular polygon.
-> This regular polygon has n-sides with same angle and length. 
-> n is the number of sides and s is the length of each sides.
-> Class and main function are created.
-> init method is used. Further accessors and mutuators are used.
-> Main method is defined and called with input validation and print statements.
'''

import math

class definition:

    def __init__(self):
        self.__nSides = 0
        self.__sLength = 0.0

    def nSides1(self, nSide):
        self.__nSides = nSide

    def sLength1(self, sLength):
        self.__sLength = sLength
    
    def nSides2(self):
        return self.__nSides

    def sLength2(self):
        return self.__sLength

    def area(self):
        area = ((self.__nSides) * ((self.__sLength) ** (2))) / ((4) * (math.tan(math.pi / self.__nSides)))
        return area

    def perimeter(self):
        perimeter = self.__nSides * self.__sLength
        return perimeter

def main():

    polygon = definition()

    nSides = int(input("Enter the number of sides (>=3): "))
    while nSides < 3:
        nSides = int(input("Invalid entry. Re-enter the number of sides (>=3): "))

    sLength = float(input("Enter the length of each sides (>=0.1): "))
    while sLength < 0.1:
        sLength = float(input("Invalid entry. Re-enter the length of each sides (>=0.1): "))

    polygon.nSides1(nSides)
    polygon.sLength1(sLength)
    
    print(f"The polygon has {polygon.nSides2()} sides. Each side is {polygon.sLength2()} units in length.")
    print(f"The perimeter of the polygon is {polygon.perimeter():.3f} units and its area is {polygon.area():.3f} square units.")

main()
