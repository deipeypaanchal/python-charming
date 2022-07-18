# Code 1
# a = input("Please enter your date of birth in mmddyyyy format: ")
# if a == ("08152003"):
#    print("Congratulations! You are Deepey Panchal")
# elif a == ("12211999"):
#    print("Hello Vrrishaa P Paanchal")
# else :
#    print("Please enter a valid date of birth")

# Code 2
# a = input("Please enter your name:")
# if a == ("Deepey"):
#    age = 18
#    print("Your age is", age)
# else:
#    print("Enter a valid name")

# Code 3
# a = input("Please enter your age: ")
# print('You are',a,'years old')

# Code 4
# a = input("Choose Monday/ Tuesday/ Wednesday to get the selling details: ").title()
# Monday = 100
# Tuesday = 200
# Wednesday = 300
# if a == ("Monday"):
#     print(F'On Monday, we sold things worth ${Monday}.')
# elif a == ("Tuesday"):
#     print(F'On Tuesday, we sold things worth ${Tuesday}.')
# elif a == ("Wednesday"):
#     print(F'On wednesday, we sold things worth ${Wednesday}.')
# else :
#     print("Our store was closed Thursday through Sunday.")


# All inputs are saved as a string unless a function such as float or int is used. Function for string is str.
# float function changes input to a floating point
# int function changes string to an integer

# Code 5 - FOR LOOP
# for i in range(1, 11):
#     print(i+1)
# FOR Loop is iteration.

# Code 6 - LIST Data Type
# Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#
# for i in range(len(Alphabets)):
#     print(Alphabets[i])

# Assignment 1 - Question 1 - Code 7 - Area of Octagon
# side_length = float(input("Enter the side length of the octagon: "))
# print(f'The area of an octagon with side length {side_length} is',2*(1+2**(1/2))*side_length*side_length)
# # ** function is used to find the square root without importing the math module
# # By using n**(1/2), where n is an integer, we can find a square root of integer n

# Code 8 - Calculating square root using math module
# import math
# a = float(input("Enter a number: "))
# print(math.sqrt(a))

# Code 9 - Calculating Volume of Cube without using math module
# a = float(input("Enter the side length of the Cube: "))
# print(a**(1/3))
# similar to the square root of any number, we can find cube root using n**(1/3), where n is an integer

# # Assignment 1 - Question 2 - Code 10 - Calculating Energy
# M = float(input("Enter the amount of water (in kg): "))
# initial_temperature = float(input("Enter the initial temperature: "))
# final_temperature = float(input("Enter the final temperature: "))
# print(f'The energy needed is', M * (final_temperature - initial_temperature) * 4184, 'Joules')

# Assignment 1 - Question 3 - Code 11 - Slope of a line
# x1 = float(input("Enter the x-coordinate for point1: "))
# y1 = float(input("Enter the y-coordinate for point1: "))
# x2 = float(input("Enter the x-coordinate for point2: "))
# y2 = float(input("Enter the y-coordinate for point2: "))
# print(f'The slope for the line that connects two points ({x1} , {y1}) and ({x2} , {y2}) is', (y2-y1)/(x2-x1))

# Assignment 1 - Question 4 - Code 12 - Area of a Flower
# r = float(input("Enter the radius of the flower: "))
# print(f'The area of the flower is', ((4 * (1/2) * 3.14159 * (r/2)**(2)) + (r**(2))))

# Assignment 2 - Question 1 - Code 13
# t = float(input("Enter the temperature in Fahrenheit: "))
# while t<=-58 or t>=41:
#     print("Temperature must be between -58F and 41F")
#     t = float(input("Please re-enter the temperature in Fahrenheit: "))
# if t>-58 or t<41:
#     w = float(input("Enter the wind speed miles per hour: "))
# while w<2:
#     print("Speed must be greater than or equal to 2")
#     w = float(input("Please re-enter the wind speed miles per hour: "))
# if w>=2:
#     i = 35.74 + 0.6215 * t - 35.75 * (w ** 0.16) + 0.4275 * t * (w ** 0.16)
#     print(f'The wind chill index is {i:.3f}')

# Assignment 2 - Question 2 - Code 14
# import random
# a = int(input("Player 1, what is your bid? "))
# b = int(input("Player 2, what is your bid? "))
# c = int(input("Player 3, what is your bid? "))
# d = int(input("Player 4, what is your bid? "))
# price = random.randint(500, 3000)
# if a > price and b > price and c > price and d > price:
#     print("Buzz! Aww... everyone has overbid!")
# elif a == price:
#     print("Ding Ding Ding! One player got it exactly right and gets $500!")
#     print(f'Actual price is ${price}! Player 1, come on up!')
# elif b == price:
#     print("Ding Ding Ding! One player got it exactly right and gets $500!")
#     print(f'Actual price is ${price}! Player 2, come on up!')
# elif c == price:
#     print("Ding Ding Ding! One player got it exactly right and gets $500!")
#     print(f'Actual price is ${price}! Player 3, come on up!')
# elif d == price:
#     print("Ding Ding Ding! One player got it exactly right and gets $500!")
#     print(f'Actual price is ${price}! Player 4, come on up!')
#
# elif a != price and b != price and c != price and d != price:
#
#     aa = (price - a)
#     bb = (price - b)
#     cc = (price - c)
#     dd = (price - d)
#
#     list_a = [aa, bb, cc, dd]
#
#     list_b = []
#
#     for x in list_a:
#         if x > 0:
#             list_b.append(x)
#
#     winner = min(list_b)
#
#     if winner == aa:
#         print(f'Actual price is ${price}! Player 1, come on up!')
#     if winner == bb:
#         print(f'Actual price is ${price}! Player 2, come on up!')
#     if winner == cc:
#         print(f'Actual price is ${price}! Player 3, come on up!')
#     if winner == dd:
#         print(f'Actual price is ${price}! Player 4, come on up!')

# Stone Paper Scissor Game - Code 15
# welcome = """
# ************************************************************
# *                                                          *
# *        Welcome to the Rock, Paper, Scissors Game!        *
# *                                                          *
# ************************************************************
# """
# print(welcome)
#
# player1 = str(input("\nPlayer 1, Please enter Rock, Paper, or Scissor: ")).title()
# player2 = str(input("\nPlayer 2, Please enter Rock, Paper, or Scissor: ")).title()
#
# if player1 == player2:
#     print("\nGame is tie. Please try again")
#
# else:
#     print("\nWrite a valid word... you bitch!!")

# Code 16 - Exercise 3 - Question 1
# number = int(input("Starting number of organisms: "))
# while number <= 0:
#     number = int(input("Starting number of organisms: "))
# increase = int(input("Average daily increase (as a %): "))
# while increase <= 0:
#     increase = int(input("Average daily increase (as a %): "))
# days = int(input("Number of days to multiply: "))
# while days <= 0:
#     days = int(input("Number of days to multiply: "))
# print(f'Day\t\t\t\tPopulation')
# print(f'--------------------------')
# for days in range(1, days + 1):
#     if days == 1:
#         print(f'{days}\t\t\t\t{number:.6f}')
#     else:
#         number = number + (number * (increase / 100))
#         print(f'{days}\t\t\t\t{number:.6f}')

# Code 17 - Exercise 3 - Question 2
# import random
# correct_number = random.randint(1, 100)
# print(correct_number)
#
# number = int(input("Enter a number between 1 and 100 (inclusive): "))
# count = 1
#
# while number > 100 or number < 0 or number > correct_number or number < correct_number:
#     if number > 100:
#         number = int(input("Very funny. Enter a number between 1 and 100 (inclusive): "))
#         count += 0
#     elif number < 0:
#         number = int(input("Really? Enter another guess between 1 to 100: "))
#         count += 0
#     elif number > correct_number:
#         number = int(input("Too high. Enter another guess: "))
#         count += 1
#     elif number < correct_number:
#         number = int(input("Too low. Enter another guess: "))
#         count += 1
#     if count == 10:
#         print(f'Sorry, the number was {count}')
#         break
#
# if number == correct_number:
#     print(f'You guessed it right!! You got it in {count} guesses!')

# Code 18 - Exercise 3 - Question 3
# import turtle

# side = int(input("Enter the number of sides between 3 and 12 (inclusive): "))
# while not 3 <= side <= 12:
#     side = int(input("Invalid number of sides. Enter the number between 3 and 12 (inclusive): "))

# length = int(input("Enter the length of each side (> 50): "))
# while length <= 50:
#     length = int(input("Please enter a larger length of each side: "))

# angle = (180 * (side - 2)) / side

# turns = 180 - angle

# for a in range(side):
#     turtle.forward(length)
#     turtle.right(turns)

# Code 19 - Exercise 3 - Question 4
# import turtle
# side = int(input("Enter the number of sides between 3 and 12 (inclusive): "))
# while not 3 <= side <= 12:
#     side = int(input("Invalid number of sides. Enter the number between 3 and 12 (inclusive): "))
# length = int(input("Enter the length of each side (> 50): "))
# while length <= 50:
#     length = int(input("Please enter a larger length of each side: "))
# angle = (180 * (side - 2)) / side
# turns = 180 - angle
# for a in range(side):
#     turtle.forward(length)
#     turtle.right(turns)
# if side == 3:
#     turtle.write('Triangle')
# elif side == 4:
#     turtle.write('Tetragon')
# elif side == 5:
#     turtle.write('Pentagon')
# elif side == 6:
#     turtle.write('Hexagon')
# elif side == 7:
#     turtle.write('Heptagon')
# elif side == 8:
#     turtle.write('Octagon')
# elif side == 9:
#     turtle.write('Nonagon')
# elif side == 10:
#     turtle.write('Decagon')
# elif side == 11:
#     turtle.write('Hendecagon')
# elif side == 12:
#     turtle.write('Dodecagon')
# turtle.done()

# Code 20 - Exercise 4 - Question 1 - Tortoise vs. Hare
# import random

# def tortoise(a):
#     moves = random.randint(1, 10)
#     if 1 <= moves <= 5:
#         return 3
#     elif 6 <= moves <= 7:
#         return -5
#     else:
#         return 1

# def hare(b):
#     moves = random.randint(1, 10)
#     if 1 <= moves <= 2:
#         return 0
#     elif 3 <= moves <= 4:
#         return 7
#     elif moves == 5:
#         return -10
#     elif 6 <= moves <= 8:
#         return 1
#     else:
#         return -2

# def race():
#     seconds = 0
#     position_t = 0
#     position_h = 0

#     while (position_t and position_h) < 50:

#         position_t = tortoise(position_t) + position_t
#         if position_t < 0:
#             position_t = 0
#         if position_t > 50:
#             position_t = 50

#         position_h = hare(position_h) + position_h
#         if position_h < 0:
#             position_h = 0
#         if position_h > 50:
#             position_h = 50

#         if position_t == position_h:
#             print(f'{(position_t - 1) * " "} OW!')
#         else:
#             if position_t == 0:
#                 position_t = 1
#             if position_h == 0:
#                 position_h = 1

#             tortoise_line = (f'{(position_t - 1) * " "} T')
#             hare_line = (f'{(position_h - 1) * " "} H')
#             tortoise_list = list(tortoise_line)
#             hare_list = list(hare_line)
#             if position_t > position_h:
#                 tortoise_list[hare_list.index('H')] = 'H'
#                 print("".join(tortoise_list))
#             elif position_h > position_t:
#                 hare_list[tortoise_list.index('T')] = 'T'
#                 print("".join(hare_list))

#         seconds += 1

#     if position_t < position_h:
#         print("Hare wins. Yay.")
#         print(f'Time of race: {seconds} seconds.')
#     else:
#         print("Tortoise wins!! Yay!")
#         print(f'Time of race: {seconds} seconds.')

# print("ON YOUR MARK... GET SET...")
# print("GO!!!!!!")
# print("AND THEY'RE OFF!")
# print()

# race()

# Code 20 - Exercise 5 - Question 1 - Magic 8 Ball
#
# import random
# list_of_responses = [
#     "It is certain.",
#     "It is decidedly so.",
#     "Without a doubt.",
#     "Yes definitely.",
#     "You may rely on it.",
#     "As I see it, yes.",
#     "Most likely.",
#     "Outlook good.",
#     "Yes.",
#     "Signs point to yes.",
#     "Reply hazy, try again.",
#     "Ask again later.",
#     "Better not tell you now.",
#     "Cannot predict now.",
#     "Concentrate and ask again.",
#     "Don't count on it.",
#     "My reply is no.",
#     "My sources say no.",
#     "Outlook not so good.",
#     "Very doubtful."
# ]
# response = random.choice(list_of_responses)
#
# question = str(input("What is your question? "))
# print(response)
#
# new_question = str(input("Would you like to ask another question? ")).casefold()
# while new_question == "yes":
#     new_response = random.choice(list_of_responses)
#     question = str(input("What is your question? "))
#     print(new_response)
#     new_question = str(input("Would you like to ask another question? ")).casefold()
#
#     if new_question == "no":
#         break

# Code 21 - Exercise 5 - Question 3
# import random
# directory1 = {
#     "Alabama": "Montgomery",
#     "Alaska": "Juneau",
#     "Arizona": "Phoenix",
#     "Arkansas": "Little Rock",
#     "California": "Sacramento",
#     "Colorado": "Denver",
#     "Connecticut": "Hartford",
#     "Delaware": "Dover",
#     "Florida":	"Tallahassee",
#     "Georgia": "Atlanta",
#     "Hawaii": "Honolulu",
#     "Idaho": "Boise",
#     "Illinois": "Springfield",
#     "Indiana": "Indianapolis",
#     "Iowa":	"Des Moines",
#     "Kansas": "Topeka",
#     "Kentucky": "Frankfort",
#     "Louisiana": "Baton Rouge",
#     "Maine": "Augusta",
#     "Maryland": "Annapolis",
#     "Massachusetts": "Boston",
#     "Michigan": "Lansing",
#     "Minnesota": "Saint Paul",
#     "Mississippi": "Jackson",
#     "Missouri":	"Jefferson City",
#     "Montana": "Helena",
#     "Nebraska":	"Lincoln",
#     "Nevada": "Carson City",
#     "New Hampshire": "Concord",
#     "New Jersey": "Trenton",
#     "New Mexico": "Santa Fe",
#     "New York": "Albany",
#     "North Carolina": "Raleigh",
#     "North Dakota": "Bismarck",
#     "Ohio": "Columbus",
#     "Oklahoma": "Oklahoma City",
#     "Oregon": "Salem",
#     "Pennsylvania": "Harrisburg",
#     "Rhode Island":	"Providence",
#     "South Carolina": "Columbia",
#     "South Dakota": "Pierre",
#     "Tennessee": "Nashville",
#     "Texas": "Austin",
#     "Utah": "Salt Lake City",
#     "Vermont": "Montpelier",
#     "Virginia": "Richmond",
#     "Washington": "Olympia",
#     "West Virginia": "Charleston",
#     "Wisconsin": "Madison",
#     "Wyoming": "Cheyenne"}

# print(answer)

# Week 13 Lecture 1 DT.04.04.2022
#Inheritance Example - Driver Program

# import Vehicle

# v1 = Vehicle.Vehicle("Hyundai", "2007 Elantra")
# print(f'\nMake: {v1.getmake()}')
# print(f'Year and Model: {v1.getyrmodel()}')

# car1 = Vehicle.Car("Honda", "2016 Accord", 4)
# print(f'\nMake: {car1.getmake()}')
# print(f'Year and Model: {car1.getyrmodel()}')
# print(f'Number of Doors: {car1.getdoors()}\n')
