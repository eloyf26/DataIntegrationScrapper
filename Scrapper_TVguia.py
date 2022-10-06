from cgitb import html
from operator import concat
from bs4 import BeautifulSoup
import requests
import re
import json

def main( htmlSource ):
    
    soup=BeautifulSoup(htmlSource,'html.parser')

    #Find the div tag that contains all the channels
    channels = soup.find_all(id = re.compile('channel-*'))

    dayScheduleInfo = []

    for channel in channels:
        workingChannel = {'name':GetChannelName(channel),'programs':[]}
        programs = channel.find_all("a","a-details")
        for tvProgram in programs:            
           
            # Find link with all info in the a tag for each of the tv programs
            #infoLink = tvProgram.attrs['href']
            #page = requests.get(domain + infoLink)
            #programSoup=BeautifulSoup(page.content,'html.parser')
            programNameAndTime = GetProgramInfo(tvProgram)
            programInfo = {'title':programNameAndTime[1], 'time':programNameAndTime[0]}
            workingChannel['programs'].append(programInfo)

        dayScheduleInfo.append(workingChannel)
    jsonInfo = json.dumps(dayScheduleInfo,sort_keys=True, indent=4)
    print(jsonInfo)
    return jsonInfo

def GetChannelName( channel ):
    nameTag = channel.find('a')
    name = nameTag.attrs['alt']
    return name

def GetProgramInfo ( program ):
    try:
        titleTag = program.text
        temp = titleTag.strip().split()
        titleAndTime = [temp[0]," ".join(temp[1:])]
        return titleAndTime
    except:
        return [None,None]
def GetProgramTime( program ):
    time = (program.find("span", "tv-hour")).text
    return time


html1 = requests.get("https://www.tvguia.es/")
main(html1.content)