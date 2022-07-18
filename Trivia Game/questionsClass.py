'''
****** Questions Class ******
-> Defining a class that has six attributes.
-> This class have an __init__ method, accessors, mutators, and __str__ method.
'''

class questions:
  
   def __init__(self, que, ans1, ans2, ans3, ans4, correctAns):
       self.que = que
       self.ans1 = ans1
       self.ans2 = ans2
       self.ans3 = ans3
       self.ans4 = ans4
       self.correctAns = correctAns
      
   def setAns1(self, ans1):
       self.ans1 = ans1
   def setAns2(self, ans2):
       self.ans2 = ans2
   def setAns3(self, ans3):
       self.ans3 = ans3  
   def setAns4(self, ans4):
       self.ans4 = ans4
   def setCorrectAns(self, correctAns):
       self.correctAns = correctAns  
         
   def getCorrectAns(self):
       return self.correctAns
   def getAns1(self):
       return self.ans1      
   def getAns2(self):
       return self.ans2
   def getAns3(self):
       return self.ans3
   def getAns4(self):
       return self.ans4
   def getQuestion(self):
       return self.que

   # __str__ method will help to format the questions as desired
   def __str__(self):
       return "{}\n1. {}\n2. {}\n3. {}\n4. {}".format(self.que, self.ans1, self.ans2, self.ans3, self.ans4)
