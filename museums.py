from bs4 import BeautifulSoup
import requests
import os
import time
from museum import museumInfo

museums_info = []

urls = ['https://museomadrid.com/museos-tematicos-en-madrid/', 'https://museomadrid.com/museos-de-arte-en-madrid/', 
        'https://museomadrid.com/salas-de-exposicion-en-madrid/']

for url in urls:
    page = requests.get(url)
    tMuseums_soup = BeautifulSoup(page.content, 'html.parser')

    rows = tMuseums_soup.find_all('div', class_ = 'card-body')
    #print(rows)

    for museum in rows:
        link = museum.find('a', href = True)['href']
        museums_info.append(museumInfo(link))
        #print(link)
        #name = museum.find('h5').text.strip()
        #print(name)

print(museums_info)
    