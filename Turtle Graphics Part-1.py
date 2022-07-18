'''
Program to draw Polygons with the turtle module.
First of all, turtle  module is imported.
user-input is prompted for the number of sides and length.
It is taken care that side is not smaller than 3 or greater than 12.
Also, taken care that the length is greater than 50.
while and for loop is used in this program.
turtle.forward(length) and turtle.right(turns) are also used to get the correct geometric shape.
'''

import turtle

side = int(input("Enter the number of sides between 3 and 12 (inclusive): "))
while not 3 <= side <= 12:
    side = int(input("Invalid number of sides. Enter the number between 3 and 12 (inclusive): "))

length = int(input("Enter the length of each side (> 50): "))
while length <= 50:
    length = int(input("Please enter a larger length of each side: "))

angle = (180 * (side - 2)) / side
turns = 180 - angle

for a in range(side):
    turtle.forward(length)
    turtle.right(turns)
