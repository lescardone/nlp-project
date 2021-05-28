#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:40:53 2021

@author: lescardone
"""

# IMPORTS
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
#from selenium.webdriver.common.keys import Keys
#import time
import re

#import pickle
import joblib
#import shutil
import pandas as pd

# OPEN PAGE AND INFINTE SCROLL -- used only once

'''
full_height = 676368
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(4)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height > 578915:
        break    


# SCROLL TO TOP

driver.execute_script('window.scrollTo(0,0)')



# FIRST PAGE OF ALL 2021 ARTICLES --> list of all article links

soup = BeautifulSoup(driver.page_source, 'lxml')
articles = soup.find_all('h2',class_='title')
link_list = [a.find('a')['href'] for a in articles]
    
try:
    shutil.copy(src='article_links' +'.joblib', dst='article_links' + '_backup.joblib')
except FileNotFoundError:
    joblib.dump(link_list,'article_links' +'.joblib')
   
'''

link_list = joblib.load('../article_links.joblib')
len(link_list)     
link_list_trial = link_list[:2]
link_list_trial

url = 'https://www.npr.org/sections/news/archive'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

article_columns = ['idx','date','category','authors','title','article_text']
article_items_df = pd.DataFrame(columns = article_columns)

for idx, link in enumerate(link_list):
        

        driver.execute_script(f'''window.open('{link}','_blank');''')
        driver.switch_to.window(driver.window_handles[1])
        page_soup = BeautifulSoup(driver.page_source,'lxml')

        
        # article raw html
        # can use keys as rows with orient = 'index' kwarg
        story_raw = page_soup.find('div',id='storytext')

        if len(story_raw) > 50:
            
            story_text = story_raw.text
            # story_clean_1 = story_text.replace('\n','')
            story_clean_1 = re.sub('\s{2,}', ' ', story_text)
            story_clean_2 = story_clean_1.strip()
            # story_clean_2 --> article text (string)
           
            
            # article title
            title = page_soup.find('div',class_='storytitle')
            title_text = title.text
            title_clean = title_text.replace('\n','')
            # title_clean --> article title (string)
            
            # article category
            try:
                category = page_soup.find('h3',class_='slug')
                category_text = category.text
                category_clean = category_text.replace('\n','')
            except AttributeError:
                authors_clean = 'None'
                print(idx,': This article does not have a category')
            # category_clean --> category (string)
            
            # article date
            date = page_soup.find('span',class_='date')
            date_clean = date.text
            # date_clean --> date (string)
            
            # article authors
            try:
                authors = page_soup.find('div',class_='byline-container--block')
                authors_processing = authors.find_all('p')
                authors_text = [author.text.replace('\n','').strip() for author in authors_processing]
            except AttributeError:
                authors_text = []
                print(idx,': This article does not have any authors')
            # authors_text --> list of authors
            
            article_items = [idx, date_clean, category_clean, authors_text, title_clean, story_clean_2]
            
            length = len(article_items_df)
            if len(article_items) == 6:
                article_items_df.loc[length] = article_items
            else:
                pass
    

        # close tab and switch back
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

article_items_df.to_csv('article_items.csv')

for idx, link in enumerate(link_list):
        

        driver.execute_script(f'''window.open('{link}','_blank');''')
        driver.switch_to.window(driver.window_handles[1])
        page_soup = BeautifulSoup(driver.page_source,'lxml')

        
        # article raw html
        # can use keys as rows with orient = 'index' kwarg
        story_raw = page_soup.find('div',id='storytext')
        
        story_raw

