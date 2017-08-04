#Tax Bracket of People with Income

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen
import datetime

#Size of table from wiki
row = 8
col = 5

tax_bracket = {}

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

    for i in range(1, col):
        k_name = table[0].find_all('th')[i].next
        tax_bracket[k_name] = {}

    for key in tax_bracket:
        print(key)

if __name__ == '__main__':
    #Prints the last element of the list
    web_parse()
