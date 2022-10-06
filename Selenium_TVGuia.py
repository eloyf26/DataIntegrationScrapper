from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re

def main2():

    idBeforeYesterday = 'button-before-yesterday'
    idYasterday = "button-yesterday"
    idToday = "button-today"
    idTomorrow = "button-tomorrow"

    driver = webdriver.Chrome()
    driver.get("https://www.tvguia.es/") 

    GetDayInfo (idBeforeYesterday, driver)
    GetDayInfo (idYasterday, driver)
    GetDayInfo (idToday, driver)
    GetDayInfo (idTomorrow, driver)
   
def GetDayInfo( thisDay, driver ):

    idTime1 = "button-00-03"
    idTime2 = "button-03-06"
    idTime3 = "button-06-09"
    idTime4 = "button-09-12"
    idTime5 = "button-12-15"
    idTime6 = "button-15-18"
    idTime7 = "button-18-21"
    idTime7 = "button-21-24"

    beforeYasterdayButton = driver.find_elements(By.ID, thisday )

    GetTimePeriodInfo(idTime1)
    GetTimePeriodInfo(idTime2)
    GetTimePeriodInfo(idTime3)
    GetTimePeriodInfo(idTime4)
    GetTimePeriodInfo(idTime5)
    GetTimePeriodInfo(idTime6)
    GetTimePeriodInfo(idTime7)

def GetTimePeriodInfo( thisTime ):
    htmlSource = GetPageSource()
    return main( htmlSource )

main()