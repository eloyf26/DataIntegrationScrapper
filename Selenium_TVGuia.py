from gettext import find
from lib2to3.pgen2 import driver
from time import sleep
from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
from Scrapper_TVguia import *

def main2():

    idBeforeYesterday = 'button-before-yesterday'
    idYasterday = "button-yesterday"
    idToday = "button-today"
    idTomorrow = "button-tomorrow"

    driver = webdriver.Chrome()
    driver.get("https://www.tvguia.es/") 
    driver.find_element(By.ID, "c-p-bn").click()
    #print(driver.find_element(By.XPATH ,"//html")

    weeklyProgram = {"day1": "", "day2": "", "day3": "", "day4": ""}

    weeklyProgram["day1"] = GetDayInfo (idBeforeYesterday, driver)
    weeklyProgram["day2"] = GetDayInfo (idYasterday, driver)
    weeklyProgram["day3"] = GetDayInfo (idToday, driver)
    weeklyProgram["day4"] = GetDayInfo (idTomorrow, driver)

    return weeklyProgram
   
def GetDayInfo( thisDayId, driver ):

    dayProgram = { "time1":"", "time2":"", "time3":"", "time4":"", "time5":"", "time6":"", "time7":"" }

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
    

    dayProgram["time1"] = GetTimePeriodInfo(idTime1, driver)
    dayProgram["time2"] = GetTimePeriodInfo(idTime2, driver)
    dayProgram["time3"] = GetTimePeriodInfo(idTime3, driver)
    dayProgram["time4"] = GetTimePeriodInfo(idTime4, driver)
    dayProgram["time5"] = GetTimePeriodInfo(idTime5, driver)
    dayProgram["time6"] = GetTimePeriodInfo(idTime6, driver)
    dayProgram["time7"] = GetTimePeriodInfo(idTime7, driver)
    dayProgram["time8"] = GetTimePeriodInfo(idTime8, driver)

    return dayProgram

def GetTimePeriodInfo( thisTimeId , driver ):
    
    thisTime = driver.find_element(By.ID, thisTimeId)
    thisTime.click()
    sleep(0.5)
    htmlSource = GetPageSource(driver)
    timePeriodInfo = main(htmlSource)

    return timePeriodInfo

def GetPageSource(driver):
    htmlcode = driver.find_element(By.TAG_NAME, "html")
    return htmlcode.get_attribute("innerHTML")

with open('json_data.json', 'w') as outfile:
   json.dump(main2(), outfile, sort_keys=True, indent=4)
