from cgi import test
from unicodedata import name
from bs4 import BeautifulSoup
import pandas as pd
import requests
def main():
    page = requests.get("https://www.tvguia.es/")

    if (page.status_code != 200):

        print("download not succesfull")
        exit
    
    soup=BeautifulSoup(page.content,'html.parser')

    channels = soup.find("div",{"id":"ajax-here"})

    dayScheduleInfo = []

    for channel in channels:
        workingChannel = {'name':GetChannelName(channel),'programs':[]}

        for tvProgram in channel.children:
            
            # Find link with all info in the a tag for each of the tv programs
            infoLink = (tvProgram.find("a")).attrs['href']

            programInfo = {'title':GetProgramTitle(infoLink), 'time':GetProgramTime(infoLink)}
            workingChannel['programs'].append(programInfo)

        dayScheduleInfo.append(workingChannel)

    print(list(channels.children))

def GetChannelName( channel ):
    nameTag = channel.find('a')
    name = nameTag.attrs['alt']
    return name

def GetProgramTitle ( link ):

    return []

def GetProgramTime( link ):
    return 
main()