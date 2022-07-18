# Program to calculate energy using the required input values from user

# Taking input for amount of water (in kg), initial temperature, and final temperature from user
m = float(input("Enter the amount of water (in kg): "))
initial_temperature = float(input("Enter the initial temperature: "))
final_temperature = float(input("Enter the final temperature: "))

# Printing the calculated energy in Joules using its correct formula
print('The energy needed is', m * (final_temperature - initial_temperature) * 4184, 'Joules')
