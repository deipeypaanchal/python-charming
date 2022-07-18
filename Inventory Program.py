'''
****** Retail Items ******
-> This program is designed to output the details of inventory in an organized format.
-> class Retail_Item is created as per instructions with three attributes namely item, amount and price.
-> __init__ and __str__ method is used. __str__ method is used to format the resulting data.
-> User is prompted for the type of item, its availability in numbers, and its price in $.
-> User is prompted for two items.
-> main method is called and our desired results are displayed.
'''

class Retail_Item:

    def __init__(self, item, amount, price):
        self.__item = item
        self.__amount = amount
        self.__price = price
    
    def __str__(self):
        return (f'{self.__item}\t\t{self.__amount}\t\t${self.__price}')

def main():
    
    item = input("Name of item 1: ")
    amount = input("Amount of item 1: ")
    price = input("Price of item 1: ")

    item1 = Retail_Item(item, amount, price)

    item = input("\nName of item 2: ")
    amount = input("Amount of item 2: ")
    price = input("Price of item 2: ")

    item2 = Retail_Item(item, amount, price)

    print("\nHere is a summary of the items you added:") 
    print("Item\t\tAmount\t\tPrice")
    print("-----------------------------------------")
    print(item1)
    print(item2)

main()



