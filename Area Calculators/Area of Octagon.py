# Program to print the area of octagon by taking the side length input from user

# Accepting side length
side_length = float(input("Enter the side length of the octagon: "))

# Printing the area using the correct formula for area of octagon
print(f'The area of an octagon with side length {side_length} is',2*(1+2**(1/2))*(side_length)**(2))
# By using n**(1/2), where n is an integer, we can find a square root of integer n
