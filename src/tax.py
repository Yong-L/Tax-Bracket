#Tax Bracket of People with Income
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen
from math import inf
import datetime
import locale

#For USD conversion to float value
locale.setlocale(locale.LC_ALL, 'en_US.UTF8')

#Number of rows and column from wiki table
col = 5 
row = 8 

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
        if wage < k:
            return wage * tax_dict[k]

#Reads the URL page
def read_page(page_url):
    #Request from Wiki
    client = uOpen(page_url)
    page_html = client.read()
    client.close()

    return page_html

#Parse as HTML
def deduction():
    #Wikipedia about Standard Deduction Page
    page_url = 'https://en.wikipedia.org/wiki/Standard_deduction'

    page_html = read_page(page_url)

#Parses as HTML
def web_parse():
    #Tax dictionary to parse through
    tax_bracket = {}
    #Wikipedia Tax Page
    page_url = 'https://en.wikipedia.org/wiki/Income_tax_in_the_United_States'

    page_html = read_page(page_url)

    #Parses the page
    page_soup = soup(page_html, "html.parser")

    year = datetime.datetime.now().year
    year_id = "Marginal_tax_rates_for_" + str(year)
    header = page_soup.find("span", {"id" : year_id }).parent
    #Find the table for the current year
    table = header.next_sibling.next_sibling

    table = table.find_all('tr')

    #Sort first by category 
    for i in range(1, col):
        category = table[0].find_all('th')[i].next
        tax_bracket[category] = {} 

    #Parse through each percentage
    for i in range(1, row):
        
        percentage = table[i].find('th').next
        taxable = table[i].find_all('td')

        counter = 0 
        for k in tax_bracket:
            t = taxable[counter].next
            
            if i < row - 1:
                #Rows have ranges instead of numbers
                tax_bracket[k][locale.atoi(t[t.index('–') + 3:])] = float(percentage[:len(percentage)-1])/100
            else:
                #Last row doesn't just has one number 
                tax_bracket[k][inf] = float(percentage[:len(percentage)-1])/100
            counter += 1

    return(tax_bracket)

if __name__ == '__main__':
    #Prints the last element of the list
    tax_dict = web_parse() 
    sub_tax = tax_dict[print_menu(tax_dict)]
    print(print_wage(sub_tax))
