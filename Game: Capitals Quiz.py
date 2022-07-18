'''
*A dictionary is created to store the names of states and their capitals as key value pairs.
*It is further converted to a list.
*While loop is used to stop the game when user insert q in either upper or lower case.
*The while loop includes an if elif structure to keep track of the user’s correct and incorrect answers.
*correct and incorrect answers are calculated and the record is released when user chooses to quit the game.
'''

import random

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"}

states_list = list(capitals.keys()) #Creating a states' list with the keys of dictionary
state = states_list[(random.randint(0,49))] #Random number generator is used to pick the state from states_list
capital = capitals[state] #Capitals of particular state
#To calculate score
correct = 0
incorrect = 0

question = str(input(f'What is the capital of {state}? (or enter q to quit): '))

while (question.lower() == capital.lower()) or (question.lower() == "q") or ((question.lower() != "q") and (question.lower() != capital.lower())):
    if question.lower() == capital.lower():
        print("That is correct.")
        correct += 1 #To calculate score
        new_state = random.choice(states_list)
        capital = capitals[new_state] 
        question = str(input(f'What is the capital of {new_state}? (or enter q to quit): '))

    elif question.lower() == "q":
        print(f'You had {correct} correct responses and {incorrect} incorrect responses.') #prints score
        break #To break the process when user wants
    
    elif (question.lower() != "q") and (question.lower != capital.lower()):
        print("That is incorrect.")
        incorrect += 1 #To calculate score
        new_state = random.choice(states_list)
        capital = capitals[new_state] 
        question = str(input(f'What is the capital of {new_state}? (or enter q to quit): '))
