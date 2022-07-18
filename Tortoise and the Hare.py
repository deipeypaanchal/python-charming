'''
*This program stimulates the classical race between the tortoise and the hare with couple modifications.
*Random function is imported first of all to get the moves of tortoise and hare as per the probability order.
*To elaborate that, int 1 to 10 is used. Lets say it is probability from percent 1 to 100.
*now to be precise, moves are determined as per the chart and int 1 to 10. (See comments with the code for better understanding)
*‘H’ and ‘T’ shows where the Hare and the Tortoise are on the course.
*While loop is used to satisfy the requirements and to get the desired results.
*Three functions in total are created: For the motion of tortoise, that for hare, and the one overall for the race.
*OW! is printed when both the animals are at the same positon. It is funny that the tortoise bites hare. (Isn't that cheating?? our program still allows them to run the race).
*hare list and tortoise list is created for perfect spaces of our output and thus further strings are joined.
* .join is used to return the joined string.
'''

import random

def tortoise(a):
    moves = random.randint(1, 10)
    if 1 <= moves <= 5:
        return 3 #Fast Plod which has a probability of 50%, which is 3 spaces forward 
    elif 6 <= moves <= 7:
        return -5 #Slip which has a probability of 20%, which is 5 spaces backward 
    else:
        return 1 # Slow Plod which has a probability of 30%, which is 1 space forward

def hare(b):
    moves = random.randint(1, 10)
    if 1 <= moves <= 2:
        return 0 #Sleep which has a probability of 20% and has No movement
    elif 3 <= moves <= 4:
        return 7 #Big Hop which has a probability of 20% and has 7 spaces forward 
    elif moves == 5:
        return -10 #Big slip which has a probability of 10% and has 10 spaces backward
    elif 6 <= moves <= 8:
        return 1 #small Hop which has a probability of 30% and has 1 space forward
    else:
        return -2 #Big slip which has a probability of 20% and has 2 spaces backward

def race():
    #below mentioned data is the statistics before the start of the race or can say at the time when the players are on mark
    seconds = 0
    position_t = 0
    position_h = 0

    while (position_t and position_h) < 50:

        position_t = tortoise(position_t) + position_t
        if position_t < 0:
            position_t = 0
        if position_t > 50:
            position_t = 50

        position_h = hare(position_h) + position_h
        if position_h < 0:
            position_h = 0
        if position_h > 50:
            position_h = 50

        if position_t == position_h:
            print(f'{(position_t - 1) * " "} OW!')
        else:
            if position_t == 0:
                position_t = 1
            if position_h == 0:
                position_h = 1

            tortoise_line = (f'{(position_t - 1) * " "} T')
            hare_line = (f'{(position_h - 1) * " "} H')

            tortoise_list = list(tortoise_line)
            hare_list = list(hare_line)

            if position_t > position_h:
                tortoise_list[hare_list.index("H")] = "H"
                print("".join(tortoise_list)) #It will return the joined string.
            elif position_h > position_t:
                hare_list[tortoise_list.index("T")] = "T"
                print("".join(hare_list)) #It will return the joined string.

        seconds += 1 #to calculate time

    if position_t < position_h:
        print("Hare wins. Yay.")
        print(f'Time of race: {seconds} seconds.')
    else:
        print("Tortoise wins!! Yay!")
        print(f'Time of race: {seconds} seconds.')

print("ON YOUR MARK... GET SET...")
print("GO!!!!!!")
print("AND THEY'RE OFF!")
print()

race()
