from gettext import find
from time import sleep
from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from Scrapper_TVguia import *



def Selenium_bot():

    idBeforeYesterday = 'button-before-yesterday'
    idYasterday = "button-yesterday"
    idToday = "button-today"
    idTomorrow = "button-tomorrow"

    driver = webdriver.Chrome()
    driver.get("https://www.tvguia.es/") 
    sleep(1)
    driver.find_element(By.ID, "c-p-bn").click()
    #print(driver.find_element(By.XPATH ,"//html")

    #weeklyProgram = {"day1": "", "day2": "", "day3": "", "day4": ""}
    weeklyProgram = []

    DayInfo1 = ["Day 1", GetDayInfo (idBeforeYesterday, driver)]
    DayInfo2 = ["Day 2", GetDayInfo (idYasterday, driver)]
    DayInfo3 = ["Day 3", GetDayInfo (idToday, driver)]
    DayInfo4 = ["Day 4", GetDayInfo (idTomorrow, driver)]

    weeklyProgram.append(DayInfo1) 
    weeklyProgram.append(DayInfo2)
    weeklyProgram.append(DayInfo3)
    weeklyProgram.append(DayInfo4)
    
    return weeklyProgram
   
def GetDayInfo( thisDayId, driver ):

    #dayProgram = { "time1":"", "time2":"", "time3":"", "time4":"", "time5":"", "time6":"", "time7":"" }
    dayProgram = []

    idTime1 = "button-00-03"
    idTime2 = "button-03-06"
    idTime3 = "button-06-09"
    idTime4 = "button-09-12"
    idTime5 = "button-12-15"
    idTime6 = "button-15-18"
    idTime7 = "button-18-21"
    idTime8 = "button-21-24"

    thisDay = driver.find_element(By.ID, thisDayId)
    thisDay.click()
    

    dayProgram.append(GetTimePeriodInfo(idTime1, driver)) 
    dayProgram.append(GetTimePeriodInfo(idTime2, driver))
    dayProgram.append(GetTimePeriodInfo(idTime3, driver))
    dayProgram.append(GetTimePeriodInfo(idTime4, driver))
    dayProgram.append(GetTimePeriodInfo(idTime5, driver))
    dayProgram.append(GetTimePeriodInfo(idTime6, driver))
    dayProgram.append(GetTimePeriodInfo(idTime7, driver))
    dayProgram.append(GetTimePeriodInfo(idTime8, driver))

    return dayProgram

def GetTimePeriodInfo( thisTimeId , driver ):
    
    thisTime = driver.find_element(By.ID, thisTimeId)
    thisTime.click()
    sleep(1)
    htmlSource = GetPageSource(driver)
    timePeriodInfo = GetTvguia(htmlSource)

    return timePeriodInfo

def GetPageSource(driver):
    htmlcode = driver.find_element(By.TAG_NAME, "html")
    return htmlcode.get_attribute("innerHTML")
