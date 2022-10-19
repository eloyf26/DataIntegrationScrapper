from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    
    programs = []

    (data, programs) = GetTimePeriodInfo(idTime1, driver, programs)
    dayProgram.append(data)
    # programs.append(program)
    (data, program) = GetTimePeriodInfo(idTime2, driver, programs)
    dayProgram.append(data)
    # programs.append(program)
    (data, programs) = GetTimePeriodInfo(idTime3, driver, programs)
    dayProgram.append(data)
    # programs.append(program)
    (data, programs) = GetTimePeriodInfo(idTime4, driver, programs)
    dayProgram.append(data)
    # programs.append(program)
    (data, programs) = GetTimePeriodInfo(idTime5, driver, programs)
    dayProgram.append(data)
    # programs.append(program)
    (data, programs) = GetTimePeriodInfo(idTime6, driver, programs)
    dayProgram.append(data)
    # programs.append(program)
    (data, programs) = GetTimePeriodInfo(idTime7, driver, programs)
    dayProgram.append(data)
    # programs.append(program)
    (data, programs) = GetTimePeriodInfo(idTime8, driver, programs)
    dayProgram.append(data)
    # programs.append(program)

    return dayProgram

def GetTimePeriodInfo( thisTimeId , driver, programs):
    
    thisTime = driver.find_element(By.ID, thisTimeId)
    thisTime.click()
    sleep(1)
    htmlSource = GetPageSource(driver)
    (timePeriodInfo, program) = GetTvguia(htmlSource, programs)

    return (timePeriodInfo, program)

def GetPageSource(driver):
    htmlcode = driver.find_element(By.TAG_NAME, "html")
    return htmlcode.get_attribute("innerHTML")

# Selenium_bot()