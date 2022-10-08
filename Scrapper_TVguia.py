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
    if (len(channels)==0):
        raise ValueError("No channels in this HTML code")

    currentScheduleInfo = []

    for channel in channels:
        #Loop through all channels

        #workingChannel will be a dictionary with the name of the channel and a list of programs
        workingChannel = {'name':GetChannelName(channel),'programs':[]}
        programs = channel.find_all("a","a-details")
        for tvProgram in programs:            
            #Loop through all programs

            #Get the time and title 
            programNameAndTime = GetProgramInfo(tvProgram)
            programInfo = {'title':programNameAndTime[1], 'time':programNameAndTime[0]}

            #Each program is a dictionary with title and time, and it will be appended to the programs list
            workingChannel['programs'].append(programInfo)

        currentScheduleInfo.append(workingChannel)

    return currentScheduleInfo

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
