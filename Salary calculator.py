'''
###### Employee Salary ######

$ This program has three types of Engineering employees with seperate pay respective of their roles.
$ This program evaluates their salary based on the number of hours they have worked.
$ Inheritance is used.
$ Input validation is used as well.

'''

class Employee:
    def __init__(self, name, employeeID):
        self.__name = name
        self.__employeeID = employeeID
    
    def setName(self):
        return self.__name

    def setEmployeeID(self):
        return self.__employeeID
    
class Engineer(Employee):
    def __init__(self, name, employeeID, title, hrWorked):
        Employee.__init__(self, name, employeeID)
        self.__title = title
        self.__hrWorked = hrWorked
        self.__payRate = 0
        self.payRate(title)
    
    def getSalary(self, title, hrWorked):
        self.__title = title
        self.__hrWorked = hrWorked
    
    def payRate(self, title):
        dictionary = {
            "Engineering Intern" : 20, 
            "Senior Engineer" : 45, 
            "Lead Engineer" : 70
            }
        self.__payRate = dictionary[title]
        return self.__payRate
    
    def weeklyPay(self):
        
        if self.__hrWorked < 40:
            regPay = self.__hrWorked * self.__payRate
            return regPay
        
        elif self.__hrWorked > 40:
            regPay = (40 * self.__payRate) + ((self.__hrWorked - 40) * 1.5 * self.__payRate) 
            return regPay
    
    def __str__(self):
        return (f"Payroll Data for employee {self.setEmployeeID()}:\n{self.setName()}'s pay this week is: ${self.weeklyPay():,.2f}")


def main():
    name = input("Enter the employee's name: ")
    employeeID = input("Enter the employee's ID number: ")
    title = input("Enter the employee's title: ")
    hrWorked = int(input("Enter the number of hours the employee worked this week: "))

    while (hrWorked < 0 or hrWorked > 60):
        hrWorked = int(input("Invalid. Hours can't be negative or greater than 60: "))
    
    engineer = Engineer(name, employeeID, title, hrWorked)

    print(engineer)

main()

