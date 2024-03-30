#!/usr/bin/env python
# coding: utf-8

# ## Scraping stats data from IPLT20 Site

# In[3]:


#import the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def collect_cricinfo():
    #setup the driver
    driver = webdriver.Chrome()

    #define the url
    url = 'https://www.iplt20.com/stats/2024'

    #open the website
    driver.get(url)
    time.sleep(3) 

    #maximize the window
    driver.maximize_window()

    #accepting the cookies
    cookies = driver.find_element(By.XPATH,'/html/body/div[3]/div/button')
    cookies.click()
    time.sleep(2)

    #scroll and click view more
    scroll = 2350
    driver.execute_script(f'window.scrollTo(0, {scroll});')
    time.sleep(4)
    view_more = driver.find_element(By.CSS_SELECTOR,"#battingTAB > div > a")
    time.sleep(2)
    view_more.click()

    #lets define the soup to collect the required data
    soup = BeautifulSoup(driver.page_source,'html.parser')
    table = soup.find('div',class_='np-mostrunsTable')

    header = [item.text.strip() for item in table.find('tr', class_='st-table__head') if item.text.strip()]
    #     print(header)

    #create a empty dataframe
    df = pd.DataFrame(columns=header)

    #collecting the row and looping inside the header

    rows = [[item.text.strip() for item in row.find_all('td')] for row in table.find_all('tr')]

    #looping the row inside header and creating dataframe
    df = pd.DataFrame(rows,columns=header)
    #droping the null values
    df1 = df.dropna()

    #lets collect image and links 
    df_link = pd.DataFrame(columns=['Player','Image','Link'])
    name = [item.text.strip() for item in table.find_all('div',class_='st-ply-name ng-binding')]
    image = [item.get('ng-src') for item in table.find_all('img') if item.get('ng-src') and "teamlogos" not in item.get('ng-src')]
    link = [item.get('href') for item in table.find_all('a',class_='st-ply')]
    dlink =  pd.DataFrame({'Player':name,'Image':image,'Link':link})
    df_link = pd.concat([dlink,df_link],ignore_index=True)

    driver.quit() #close the browser window

    df1.to_csv(r'D:\Program\New folder\ipl201.csv')
    
    df_link.to_csv(r'D:\Program\New folder\ipl202.csv')
    
    return print('file saved in the given path')


# In[4]:


collect_cricinfo()


# In[ ]:




