'''
*This program prompts the user for several integers as well as a limit.
*The program displays the number of values that are less than the specified limit. 
*The main function is explicitely defined and called.
*Main function includes an empty list, and the code to prompt the user for the size of the list, numbers, and the limit.
*lesser_numbers function accepts the list and the limit as parameters. It includes a loop for iterating over the list.
*Empty list in the main function is filled by the user.
*The user is asked for the size of the list.
*For loop is used with the append method to fill the list to the appropriate size.
'''

#void function
def lesser_numbers(a, limit):
    list1 = []
    for x in a:
        if x < limit:
            list1.append(x)
    list_of_numbers = ' '.join([str(y) for y in list1])
    print(f'{list_of_numbers} are less than the limit {limit}')

#main function
def main():
    list2 = []
    compare = int(input('How many numbers will you compare?: '))
    for x in range(compare):
        number = int(input('Enter a number: '))
        list2.append(number) #adding the numbers to the list
    user_limit = int(input('What is the limit?: ')) #prompting user for the limit
    lesser_numbers(list2, user_limit)

main()
