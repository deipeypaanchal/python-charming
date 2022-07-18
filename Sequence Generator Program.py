'''
This program offers the users a menu and asks them to select a sequence they would like to see from the choices of Fibonacci sequence, Catlan sequence, and the Lazy Caterer's sequence. User inputs the number of values they want for a sequence and the program displays all the values of a sequence as a list until that order's value.
'''
import math

def display_menu():
    print("\nWelcome to the number sequence generator program!")
    print("Here are your choices:")
    print("1. Fibonacci Sequence")
    print("2. Catalan Sequence")
    print("3. Lazy Caterer's Sequence")

def fibonacci(num_val):
    result = [0,1]
    while len(result) < num_val:
        new=result[-1] + result[-2]
        result.append(new)
    return result

def catalan(num_val):
    result = []
    for x in range(0, num_val):
        result.append(int(((math.factorial(2 * x))/ ((math.factorial(x+1)) * (math.factorial(x))))))
    return result

def lazy_caterer(num_val):
    result = []
    for x in range(0, num_val):
        result.append(int((((x**2)+(x)+(2))/2)))
    return result

quit = False

while not quit:
    
    display_menu()

    choice = int(input("Enter your choice (1 - 3): "))

    while choice <1 or choice > 3:
        choice = int(input("Invalid entry. Re-enter your choice (1 - 3): "))
    
    num_val = int(input("Enter the number of values for the list (>=3): "))

    while num_val < 3:
        num_val = int(input("Invalid entry. Re-enter the number of values for the list: "))

    if choice == 1:
        print("Here's a list containing the first ", num_val, "of the Fibonacci Sequence: ", fibonacci(num_val))
    elif choice == 2:
        print("Here's a list containing the first ", num_val, "of the Catalan Sequence: ", catalan(num_val))
    elif choice == 3:
        print("Here's a list containing the first ", num_val, "of the Lazy Caterer's Sequence: ", lazy_caterer(num_val))

    que = str(input("Would you like to run the program again? Enter yes or no: "))

    if que.lower() == "no":
        quit = True
        print("Thanks for using the program! Goodbye!")
        continue

