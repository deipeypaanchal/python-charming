'''
****** Trivia Questions ******
-> Function is created which contains the list of questions.
-> Importing the module that contains the class definition for the questions.
'''

from questionsClass import questions

def getQuestionsList():

   questionsList = []

   questionsList.append(questions("How many days are in a lunar year?", "354", "365", "243", "379", 1))
   questionsList.append(questions("What is the largest planet?", "Mars", "Jupiter", "Earth", "Pluto", 2))
   questionsList.append(questions("What is the largest kind of whale?", "Orca whale", "Humpback whale", "Beluga whale", "Blue whale", 4))
   questionsList.append(questions("Which dinosaur could fly?", "Triceratops", "Tyrannosaurus Rex", "Pteranodon", "Diplodocus", 3))
   questionsList.append(questions("Which of these Winnie the Pooh characters is a donkey?", "Pooh", "Eeyore", "Piglet", "Kanga", 2))
   questionsList.append(questions("Which is the hottest planet?", "Mars", "Pluto", "Earth", "Venus", 4))
   questionsList.append(questions("Which dinosaur had the largest brain compared to body size?", "Troodon", "Stegosaurus", "Ichthyosaurus", "Gigantoraptor", 1))
   questionsList.append(questions("What is the largest type of penguins?", "Chinstrap penguins", "Macaroni penguins", "Emperor penguins", "White-flippered penguins", 3))
   questionsList.append(questions("Which children's story character is a monkey?", "Winnie the Pooh", "Curious George", "Horton", "Goofy", 2))
   questionsList.append(questions("How long is a year on Mars?", "550 Earth days", "498 Earth days", "126 Earth days", "687 Earth days", 4))
  
   return questionsList
