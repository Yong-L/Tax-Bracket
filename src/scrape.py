from bs4 import BeautifulSoup as soup
from page import read_page
from math import inf
import datetime

#Number of rows and column for first table
col = 5
row = 8

#Parses as HTML
def bracket():
    #Tax dictionary to parse through
    tax = {}
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
        tax[category] = {} 

    #Parse through each percentage
    for i in range(1, row):
        
        percentage = table[i].find('th').next
        taxable = table[i].find_all('td')

        counter = 0 
        for k in tax:
            t = taxable[counter].next
            
            if i < row - 1:
                #Rows have ranges instead of numbers
                tax[k][t[t.index('–') + 3:].replace(',','')] = float(percentage[:len(percentage)-1])/100
            else:
                #Last row doesn't just has one number 
                tax[k][inf] = float(percentage[:len(percentage)-1])/100
            counter += 1

    return(tax)

def deduction():
    #Wiki page about Standard Deduction in U.S
    page_url = "https://en.wikipedia.org/wiki/Standard_deduction"

    #Parse HTML
    page_html = read_page(page_url)
    page_soup = soup(page_html, 'html.parser')

    #Now search for table
    div_body = page_soup.find('div', {'id' : 'content'}, {'class' : 'mw-body'})

    div_bodyContent = div_body.find('div', {'id' : 'bodyContent'}, {'class' :
                                                       'mw-body-content'})
    div_contentText = div_bodyContent.find('div', {'id' : 'mw-content-text'},
                                            {'class',
                                             'mw-content-ltr'}).find('div',
                                                                     {'class' :
                                                                      'mw-parser-output'})

    table = div_contentText.find('table', {'class' :
                                           'wikitable'})
    cur_year = datetime.datetime.now().year

    deduc_dict = {}

    for tr in table.find_all('tr'):
        if tr.find('th') != None and tr.find('th').next == 'Year':
            for th in tr.find_all('th'):
                if th.next == 'Qualifying Surviving Spouse':
                    deduc_dict['Qualified Widow'] = None
                    continue
                deduc_dict[th.next] = None

    for tr in table.find_all('tr'):
        if tr.find('td') != None and tr.find('td').next == str(cur_year):
            for td, key in zip(tr.find_all('td'), deduc_dict):
                deduc_dict[key] = td.next.replace(',','').replace('$','')

    return deduc_dict
