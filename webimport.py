import requests
from bs4 import BeautifulSoup
import time

url = 'https://no.wikipedia.org/wiki/Liste_over_norske_etternavn'
url='https://no.wikipedia.org/wiki/Liste_over_norske_dobbeltnavn'
url = 'https://no.wikipedia.org/wiki/Kategori:Navn_med_norrøn_opprinnelse'
url = 'https://no.wikipedia.org/wiki/Liste_over_kvinnenavn_med_norrøn_opprinnelse'

url = 'https://snl.no/.taxonomy/4133'

url = 'https://no.wikipedia.org/wiki/Liste_over_norske_mannsnavn'

def gethtml(url):
    r = requests.get(url)
    return r.text
def getsoup(url):
    html = gethtml(url)
    soup = BeautifulSoup(html,'html.parser')
    return soup

def snl_taxonomy(url):
    #Norske ord og uttrykk
    url = 'https://snl.no/.taxonomy/4133'
    soup = getsoup()
    tax = soup.find_all('div',class_='l-taxonomy__contents')
    lis = tax[0].find_all('li')
    items = [l.text.strip() for l in lis]
    return items

def tilfeldig():
    url = 'https://no.wikipedia.org/wiki/Spesial:Tilfeldig'
    soup = getsoup(url)
    return soup

def check_tilfeldig():
    soup = tilfeldig()
    return soup

def rows(soup):
    rowcount = soup.find_all('tr')
    return len(rowcount)
    
def monitor():

    while True:
        global soup
        soup = check_tilfeldig()
        global tabledata 
        tabledata = rows(soup)
        global title
        title = soup.title.text
        with open(f'soupdir/{title}','w', encoding='utf-8') as f:
            soupstr = str(soup)
            print(f'Writing {len(soupstr)} lines to {title} ({tabledata} rows)')
            f.write(soupstr)
        time.sleep(10)


def main():
    monitor()

if __name__ == '__main__':
    main()

