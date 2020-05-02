import pandas as pd
path = 'I:\\webscraping\\Downloads\\'#ticker file path
df = pd.read_csv(path+'NSE50.csv')
tickers = df['Symbol'].unique()
print(tickers)
def home(driver, ticker):
    driver.get("https://www.nseindia.com/products/content/equities/equities/eq_security.htm")

    symbol =driver.find_element_by_name('symbol')
    symbol.send_keys(ticker)


    ele = driver.find_element_by_id('rdDateToDate')
    ele.click()
    
def dates(driver, start_date, end_date ):
    #start_date = '01-06-2018'
    #end_date = '01-05-2019'
    driver.find_element_by_id('fromDate').clear()
    sd = driver.find_element_by_id('fromDate')
    sd.send_keys(start_date)

    driver.find_element_by_id('toDate').clear()
    ed = driver.find_element_by_id('toDate')
    ed.send_keys(end_date)

    res = driver.find_element_by_class_name('getdata-button')
    res.click()
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

for ticker in tickers:
    chrome_options = webdriver.ChromeOptions()
    download_path = os.path.join('I:\webscraping\Downloads',str(ticker))#download path
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    prefs = {'download.default_directory' : download_path}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome('C:\\Users\\veeru\\chrome\\chromedriver.exe', options=chrome_options)#chomedriver path
    
    home(driver, ticker)
    time.sleep(1)
    for i in range(10):
        if i==0:
            end_date = date.today().strftime("%d-%m-%Y")
            start_date = (date.today()-relativedelta(years=1)+timedelta(days=1)).strftime("%d-%m-%Y")
            temp_st = date.today()-relativedelta(years=1)+timedelta(days=1)
        dates(driver, start_date=str(start_date), end_date=str(end_date))
        end_date = start_date
        temp_st = temp_st-relativedelta(years=1)+timedelta(days=1)
        start_date = temp_st.strftime("%d-%m-%Y")
        delay = 10
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'download-data-link')))
        except Exception as e:
            with open('norecordsfound.txt', 'a') as f:
                f.write(str(start_date) + '-' + str(end_date) + ' ticker ' +'no record found')
                f.write('\n')
            print(str(start_date) + '-' + str(end_date) + ' ticker ' +'no record found')
            continue
        time.sleep(2)
        download = driver.find_element_by_class_name('download-data-link')
        download.click()
    time.sleep(2)
    driver.close()
    