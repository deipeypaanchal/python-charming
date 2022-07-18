'''
****** Driver Program ******
-> The program is created that executes the trivia game based on the list of trivia questions.
-> This module imports the module used to generate and return a list of trivia questions.
-> The game is working as desired and the scores are displayed.  
'''

from triviaQuestions import getQuestionsList
from questionsClass import questions
def main():

   p1Score = 0
   p2Score = 0
   p1Turn = True
  
   q = getQuestionsList()
   a = 0

   while a < len(q):
       if p1Turn:
           print("Question for the first player:")
       else:
           print("Question for the second player:")
      
       print(q[a])

       solution = int(input("Enter your solution (a number between 1 and 4): "))

       if solution == q[a].getCorrectAns():
           print("That is the correct answer.")

           if p1Turn:
               p1Score += 1
           else:
               p2Score += 1
       else:
           print("That is incorrect. The correct answer is {}".format(q[a].getCorrectAns()))
      
       print("")
       a += 1
       p1Turn = not p1Turn
  
   print("The first player earned {} points.".format(p1Score))
   print("The second player earned {} points.".format(p2Score))
  
   if p1Score == p2Score:
       print("The game ended in a tie.")
   elif p1Score > p2Score:
       print("The second player wins the game.")
   else:
       print("The second player wins the game.")
    
if __name__ == "__main__":
   main()      
