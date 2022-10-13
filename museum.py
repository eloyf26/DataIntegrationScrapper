from bs4 import BeautifulSoup
import requests
import os
import time

#url = 'https://museomadrid.com/museo-thyssen/'


def museumInfo(url):

    museum_info = []

    page = requests.get(url)
    museum = BeautifulSoup(page.content, 'html.parser')

    #Museum name
    try:
        name = museum.find('h1').text.strip()
        museum_info.append(name)
    except:
        name = None
        museum_info.append(name)

    #Museum image
    try:
        image = museum.find('div', class_ = 'post-thumbnail').find('img')['src']
        museum_info.append(image)
    except:
        image = None
        museum_info.append(image)

    info = description = museum.find('div', class_ = 'entry-content').find_all('p')
    #print(info)
    #Museum description
    try:
        description = info[0].text.strip()
        museum_info.append(description)
    except:
        description = None
        museum_info.append(description)

    #Museum address
    try:
        address = info[1].text.split()[1:]
        address = " ".join(address)
        museum_info.append(address)
    except:
        address = None
        museum_info.append(address)

    #How to get there
    try:
        transport = info[2].text.split()[2:]
        transport = " ".join(transport)
        museum_info.append(transport)
    except:
        transport = None
        museum_info.append(transport)

    #Contact information
    try:
        contact = info[3].text.split()
        contact = " ".join(contact)
        museum_info.append(contact)
    except:
        contact = None
        museum_info.append(contact)

    #Visit hours
    try:
        hours = info[4].text.strip()
        museum_info.append(hours)
    except:
        hours = None
        museum_info.append(hours)

    #Ticket prices
    try:
        ticket = info[5].text.strip()
        museum_info.append(ticket)
    except:
        ticket = None
        museum_info.append(ticket)

    return museum_info

