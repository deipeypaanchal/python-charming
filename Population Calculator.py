'''
This is a program to determine the Population of Organisms using the while and for loop.
If-else statements are also used in this program to fulfill its functionality.
User is prompt for the input for initial number of organisms, average rate of increase, and total days.
Input-validation is correctly used in this program.
Formula to calculate is also outputing the desired and correct values.
days + 1 is used so that we can get the desired range.
:.6f is used for desired decimal requirements.
'''

number = int(input("Starting number of organisms: "))
while number <= 0:
    number = int(input("Starting number of organisms: "))
increase = int(input("Average daily increase (as a %): "))
while increase <= 0:
    increase = int(input("Average daily increase (as a %): "))
days = int(input("Number of days to multiply: "))
while days <= 0:
    days = int(input("Number of days to multiply: "))
print(f'Day\t\tPopulation')
print(f'--------------------------')
for days in range(1, days + 1):
    if days == 1:
        print(f'{days}\t\t{number:.6f}')
    else:
        number = number + (number * (increase / 100))
        print(f'{days}\t\t{number:.6f}')
