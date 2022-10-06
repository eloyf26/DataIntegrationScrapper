from cgi import test
from pickle import FALSE, TRUE
from re import X
from sre_compile import isstring
from unicodedata import name
from bs4 import BeautifulSoup
import requests
import re
import json

from macpath import join
def main():

    domain = "https://www.tvguia.es/"
    page = requests.get(domain)

    if (page.status_code != 200):

        print("download not succesfull")
        exit
    
    soup=BeautifulSoup(page.content,'html.parser')

    #Find the div tag that contains all the channels
    channels = soup.find_all(id = re.compile('channel-*'))

    dayScheduleInfo = []

    for channel in channels:
        workingChannel = {'name':GetChannelName(channel),'programs':[]}
        programs = channel.find_all("a","a-details")
        for tvProgram in programs:            
           
            # Find link with all info in the a tag for each of the tv programs
            infoLink = tvProgram.attrs['href']
            page = requests.get(domain + infoLink)
            programSoup=BeautifulSoup(page.content,'html.parser')

            programInfo = {'title':GetProgramTitle(programSoup), 'time':GetProgramTime(programSoup)}
            workingChannel['programs'].append(programInfo)

        dayScheduleInfo.append(workingChannel)
    jsonInfo = json.dumps(dayScheduleInfo)
    print(jsonInfo)

def GetChannelName( channel ):
    nameTag = channel.find('a')
    name = nameTag.attrs['alt']
    return name

def GetProgramTitle ( program ):
    titleWithBlanks = (program.find("div", "title-details-television")).text
    title = " ".join(titleWithBlanks.split())
    return title

def GetProgramTime( program ):
    time = (program.find("span", "date-details-television")).text
    return time
main()