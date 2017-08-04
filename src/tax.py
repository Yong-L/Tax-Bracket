#Tax Bracket of People with Income
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen
from math import inf
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF8')

#Number of rows and column from wiki table
col = 5 
row = 8 

#Dictionary to parse through 
tax_bracket = {}

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
                tax_bracket[k][locale.atoi(t[t.index('–') + 3:])] =  percentage
            else:
                tax_bracket[k][inf] =  percentage
            counter += 1


    print(tax_bracket)

if __name__ == '__main__':
    #Prints the last element of the list
    web_parse()
