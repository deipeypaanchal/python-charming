'''
*This program prompts the user for a question and gives a random response from the list of 20 standard responses.
*A random number generator is used to correspond to one of the responses on that list.
*The responses function prints the response and contains a local list of standard responses.
*The main function is explicitly defined and called. It includes the prompt for a question, the code to generate a random number, and the loop to repeat the process. 
*.casefold() method is used to ensure that the code accepts all versions of the word ‘no’ and 'yes'.
*The while loop is used to continue the process of asking questions until the user wants to quit the game.
'''

import random

#void function
def responses(a):
    list_of_responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    print(list_of_responses[a])

#main function
def main():
    question = str(input("What is your question? "))
    a = random.randint(0, 19) #Random number generator
    responses(a)
    new_question = str(input("Would you like to ask another question? ")).casefold()
    while new_question == "yes":
        question = str(input("What is your question? "))
        a = random.randint(0, 19)
        responses(a)
        new_question = str(input("Would you like to ask another question? ")).casefold()
        if new_question == "no":
            break

#calling main function
main()
