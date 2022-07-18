'''
This is a program to obtain wind-chill temperature using its correct formula and user-input values of temperature and windspeed. 
This program is designed in such a way that the temperature input must be in the range of -58F and 41F.
The wind speed must be greater than or equal to 2 mph. 
while loops and if functions are used to get the desired results. Final answer contains only three decimal values.
'''

#taking input for the value of temperature within range of -58F to 41F
t = float(input("Enter the temperature in Fahrenheit: "))
#inserting while loop to ask user input whenever invalid value is inserted
while t<=-58 or t>=41:
    print("Temperature must be between -58F and 41F")
    t = float(input("Please re-enter the temperature in Fahrenheit: "))
#using if function to further take the input for wind speed only when the temperature satisfies the range of -58f and 41F
if t>-58 or t<41:
    w = float(input("Enter the wind speed miles per hour: "))
#Again inserting while loop to ask for input whenever invalid value for wind speed is inserted
while w<2:
    print("Speed must be greater than or equal to 2")
    w = float(input("Please re-enter the wind speed miles per hour: "))
#using if function to calculate wind-chill temperature with correct value and formula
if w>=2:
    i = 35.74 + 0.6215 * t - 35.75 * (w ** 0.16) + 0.4275 * t * (w ** 0.16)
    print(f'The wind chill index is {i:.3f}')
