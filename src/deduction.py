from bs4 import BeautifulSoup as soup
from page import read_page
import datetime

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

    basic_deduc = None

    for tr in table.find_all('tr'):
        if tr.find('td') != None and tr.find('td').next == str(cur_year):
            basic_deduc = tr
    
    category = None

    for tr in table.find_all('tr'):
        if tr.find('th') != None and tr.find('th').next == 'Year':
            category = tr

    print(category)
