from urllib.request import urlopen as uOpen

def read_page(page_url):
    #Request page
    client = uOpen(page_url)
    page_html = client.read()
    client.close()

    return page_html

