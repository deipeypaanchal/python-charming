'''
*This program is designed to determine whether a point is within, on, or outside a circle.
*Firstly, user input for the coordinates of the center of the circle is asked.
*Further, the input data for the radius of circle and the coordinates of point are asked.
*The distance between the center and the point is calculated using the correct formula and syntax.
*Difference between distance and radius is used to decide whether the points are within, on, or outside the circle.

*For better understanding of this program:
    Center coordinates are (x1,y1)
    Radius is 'r'
    Coordinates of point are (x2,y2)
    and the distance between the center and the point is 'd'

*if-else function is used to satisfy our demand and make the program run correctly.
'''

x1 = float(input("Enter the x-coordinate of the center of the circle: "))
y1 = float(input("Enter the y-coordinate of the center of the circle: "))

r = float(input("Enter the radius of the circle: "))
if r <= 0:
   r = float(input("Invalid. Please re-enter radius of the circle: "))

x2 = float(input("Enter the x-coordinate of the point: "))
y2 = float(input("Enter the y-coordinate of the point: "))

d = ((x2 - x1)**(2) + (y2 - y1)**(2))**(1/2)

print(f'The distance between the center {(x1,y1)} and the point {(x2,y2)} is {d:.2f}.')

if d < r:
    print(f'The point {x2,y2} is inside of the circle.')

elif d == r:
    print(f'The point {x2, y2} is on the circle.')

elif d > r:
    print(f'The point {x2,y2} is outside of the circle.')
