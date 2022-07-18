'''
This program is designed for a fascinating Good ol’ Guessing Game.
The random module is imported to get the correct number in the desired range of 1 to 100.
User is prompted for the total of 10 times (excluding invalid inputs).
When the user guesses correct answer, they win.
If they fail to determine the exact integer by the end of tenth attempt, they loses.
while loop is used for the input-validation.
if-elif statements are really helpful to run the program as per our needs.
break is used as we don't want user to input more than 10 times.
break helps to stop asking for the input from user.
We are congratulating the player as they guesses the correct number.
We are also revealing the number of attempts they did using the count variable defined in the early stage of program.
'''

import random
correct_number = random.randint(1, 100)

number = int(input("Enter a number between 1 and 100 (inclusive): "))
count = 1

while number > 100 or number < 0 or number > correct_number or number < correct_number:
    if number > 100:
        number = int(input("Very funny. Enter a number between 1 and 100 (inclusive): "))
        count += 0
    elif number < 0:
        number = int(input("Really? Enter another guess between 1 to 100: "))
        count += 0
    elif number > correct_number:
        number = int(input("Too high. Enter another guess: "))
        count += 1
    elif number < correct_number:
        number = int(input("Too low. Enter another guess: "))
        count += 1
    if count == 10:
        print(f'Sorry, the number was {count}')
        break

if number == correct_number:
    print(f'You guessed it right!! You got it in {count} guesses!')
