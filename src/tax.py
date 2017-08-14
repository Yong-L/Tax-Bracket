#Tax Bracket of People with Income
from scrape import *

#Print the selection menu
def print_menu(tax_dict):

    selection = {}

    for i, k in enumerate(tax_dict):
        selection[i+1] = k

    counter = 1
    for k,v in selection.items():
        print('{} : {}'.format(k, v))
        counter +=1

    user_input = int(input('Choose one that falls in the criteria by number: '))

    while user_input not in selection:
        user_input = int(input('Error in input please choose again: '))

    return selection[user_input]

def print_wage(tax_dict):

    wage = int(input('Input your taxable income: '))

    #Go through tax dictionary and compare which one it falls under
    for k in tax_dict:
        if wage < int(k):
            return wage * tax_dict[k]


if __name__ == '__main__':
    #Prints the last element of the list
    tax = bracket() 
    deduc = deduction()
    sub_tax = tax[print_menu(tax)]
   print(print_wage(sub_tax))
