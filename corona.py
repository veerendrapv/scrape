import pandas as pd
path = 'I:\\webscraping\\Downloads\\'#ticker file path
# df = pd.read_csv(path+'NSE50.csv')
# tickers = df['Symbol'].unique()
# print(tickers)
import pandas as pd 
def home2(driver, year):
    df = pd.read_html('https://www.worldometers.info/coronavirus/', attrs={'main_table_countries_today':'table'})
    print(df)
def home(driver, year):

    # #go to website
    driver.get(r"https://www.worldometers.info/coronavirus/")
    #select year
    userDate = driver.find_element_by_id('main_table_countries_today')
    print(userDate.text)
    # print('DONE')
    # data = driver.page_source
    # # print(data)
    # print('DONE')
    # with open("I:\\webscraping\\down\\"+ str(year) +"savecar.html", "w+") as f:
    #     f.write(data)
        
  
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
    