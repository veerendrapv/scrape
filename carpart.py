import pandas as pd
path = 'I:\\webscraping\\Downloads\\'#ticker file path
# df = pd.read_csv(path+'NSE50.csv')
# tickers = df['Symbol'].unique()
# print(tickers)
def home(driver, year):
    #go to website
    driver.get(r"http://car-part.com/")
    #select year
    userDate = driver.find_element_by_name('userDate')
    userDate.send_keys(year)

    # userDate2 =driver.find_element_by_name('userDate2')
    # userDate2.send_keys('2020')

    # select model
    userModel = driver.find_element_by_name('userModel')
    userModel.send_keys('Chevy Truck-Avalanche 1500')

    #select vehicle part
    userPart = driver.find_element_by_name('userPart')
    userPart.send_keys('Engine')

    #select location
    userPreference = driver.find_element_by_name('userLocation')
    userPreference.send_keys('USA')

    #sort by preference
    userPreference = driver.find_element_by_name('userPreference')
    userPreference.send_keys('Part Grade')

    #search based on above attributes
    dbModel = driver.find_element_by_name('Search Car Part Inventory')
    dbModel.click()

    #select required things and click
    dbModel = driver.find_element_by_name('Search Car Part Inventory')
    dbModel.click()

    x = driver.find_element_by_class_name('larger')
    print(x)
    elements = driver.find_elements_by_tag_name('table')
    print(elements)
    for els in elements:
        x = els.find_elements_by_tag_name('a')

        print(x)
        for i in x:
            print('links by veeru ', i.get_attribute("href"))


    data = driver.page_source
    with open("I:\\webscraping\\down\\"+ str(year) +"cardetails.html", "w+") as f:
        f.write(data)
        
  
import urllib
from selenium import webdriver
import time
import traceback
import os
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


years = ['2005',]#2006
for year in years:
    chrome_options = webdriver.ChromeOptions()
    # download_path = os.path.join('I:\webscraping\Downloads',str(year))#download path
    # if not os.path.exists(download_path):
    #     os.mkdir(download_path)
    # prefs = {'download.default_directory' : download_path}
    # chrome_options.add_experimental_option('prefs', prefs)
    path = 'C:\\Users\\veeru\\chrome\\chromedriver.exe'
    driver = webdriver.Chrome(path, options=chrome_options)#chomedriver path
    try:

        home(driver, year)
    except Exception as e:
        driver.close()
        raise
    driver.close()
    