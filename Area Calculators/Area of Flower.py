# Program to calculate area of flower (consisting of 4 semicircle and 1 square) using its radius

# Accepting the radius of flower
r = float(input("Enter the radius of the flower: "))

# Printing the area
# Total Area = Area of 4 semicircles + Area of square
# Area of 4 semicircles = Area of 2 circles
print('The area of the flower is', ((2 * 3.14159 * (r/2)**(2)) + (r**(2))))
