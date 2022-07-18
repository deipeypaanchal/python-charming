'''
This is a program for the game 'The Price is Right'. Random number is generated to fix the actual price and start the game.
Input value is taken from four players. Message is printed if everyone overbids. 
Message is also printed when any player insert the exact price.
If everyone underbids, then the closest value caller is considered winner. min() is used for that purpose.
If some players overbids, some underbids, or no one calls an exact bid then the closet value caller is considered winner.
'''

#importing random module to get a random integer for our program
import random

#using random module and setting range of 500 to 3000 to get a random actual price
price = random.randint(500, 3000)

a = int(input("Player 1, what is your bid? "))  #player1 bid input
b = int(input("Player 2, what is your bid? "))  #player2 bid input
c = int(input("Player 3, what is your bid? "))  #player3 bid input
d = int(input("Player 4, what is your bid? "))  #player4 bid input

#using if function to print message if everyone overbids
if a > price and b > price and c > price and d > price:
    print("Buzz! Aww... everyone has overbid!")

#using elif function to print messgae if any player bids the exact price
elif a == price:
    print("Ding Ding Ding! One player got it exactly right and gets $500!")
    print(f'Actual price is ${price}! Player 1, come on up!')
elif b == price:
    print("Ding Ding Ding! One player got it exactly right and gets $500!")
    print(f'Actual price is ${price}! Player 2, come on up!')
elif c == price:
    print("Ding Ding Ding! One player got it exactly right and gets $500!")
    print(f'Actual price is ${price}! Player 3, come on up!')
elif d == price:
    print("Ding Ding Ding! One player got it exactly right and gets $500!")
    print(f'Actual price is ${price}! Player 4, come on up!')

elif a != price and b != price and c != price and d != price:

    #finding differences
    aa = (price - a)
    bb = (price - b)
    cc = (price - c)
    dd = (price - d)

    #listing the differences
    list_a = [aa, bb, cc, dd]

    #creating a new list where negative values which also happens to be the overbids are removed
    list_b = []
    for x in list_a:
        if x > 0:
            list_b.append(x)

    #defining winner as the bid with least difference
    winner = min(list_b)

    #using if function to print
    if winner == aa:
        print(f'Actual price is ${price}! Player 1, come on up!')
    if winner == bb:
        print(f'Actual price is ${price}! Player 2, come on up!')
    if winner == cc:
        print(f'Actual price is ${price}! Player 3, come on up!')
    if winner == dd:
        print(f'Actual price is ${price}! Player 4, come on up!')
