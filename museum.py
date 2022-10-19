from bs4 import BeautifulSoup
import requests
import os
import time
import re

def get_museums(url):

    all_info = []

    page = requests.get(url)
    museums = BeautifulSoup(page.content, 'html.parser')

    all_museums = museums.find_all('div', class_ = 'listicle-item')

    for mus in all_museums:

        museum_info = []

        #Museum name
        try:
            name = mus.find('h2').text.strip()
            museum_info.append(name)
        except:
            name = None
            museum_info.append(name)

        #Interesting fact
        try:
            interest = mus.find('h3').text.strip()
            museum_info.append(interest)
        except:
            interest = None
            museum_info.append(interest)

        #Museum image
        try:
            img = mus.find('img')['data-lazy-src']
            museum_info.append(img)
        except:
            img = None
            museum_info.append(img)

        #Museum category
        try:
            category = mus.find('ul').text.strip()
            museum_info.append(category)
        except:
            category = None
            museum_info.append(category)

        #Museum description
        try:
            description = mus.find('div', class_ = 'description-wrap').text.strip()
            museum_info.append(description)
        except:
            description = None
            museum_info.append(description)

        additional = mus.find('div', class_ = 'info-bullet-wrap').find_all('p')
        
        #Museum address
        try:
            street = additional[0].text.strip()
            street = re.sub("Dirección: ","",street)
            museum_info.append(street)
        except:
            street = None
            museum_info.append(street)

        #Visiting hours
        try:
            visit_h = additional[1].text.strip()
            visit_h = re.sub("Horario: ","",visit_h)
            museum_info.append(visit_h)
        except:
            visit_h = None
            museum_info.append(visit_h)

        #Museum telephone number
        try:
            telephone = additional[2].text.strip()
            telephone = re.sub("Teléfono: ","",telephone)
            museum_info.append(telephone)
        except:
            telephone = None
            museum_info.append(telephone)

        all_info.append(museum_info)

    return all_info