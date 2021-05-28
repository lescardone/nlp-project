#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:01:22 2021

@author: lescardone
"""
# IMPORTS
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
#from selenium.webdriver.common.keys import Keys
#import time
#import re

#import pickle
import joblib
import shutil

link_list = joblib.load('article_links.joblib')
len(link_list)  

# START HERE    

url = 'https://www.npr.org/sections/news/archive'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

# ONE ARTICLE
tab = link_list[2]
driver.execute_script(f'''window.open('{tab}','_blank');''')
driver.switch_to.window(driver.window_handles[1])
page_soup = BeautifulSoup(driver.page_source,'lxml')

# article text
story_raw = page_soup.find('div',id='storytext')
story_list = []
story_list.append(story_raw) 

"""
story_text = story.text
story_clean_1 = story_text.replace('\n','')
story_clean_2 = re.sub('\s{2,}', ' ', story_clean_1)
# story_clean_2 --> article text (string)
"""

# article title
title = page_soup.find('div',class_='storytitle')
title_text = title.text
title_clean = title_text.replace('\n','')
# title_clean --> article title (string)

# article category
category = page_soup.find('h3',class_='slug')
category_text = category.text
category_clean = category_text.replace('\n','')
# category_clean --> category (string)

# article date
date = page_soup.find('span',class_='date')
date_clean = date.text
# date_clean --> date (string)

# article authors
authors = page_soup.find('div',class_='byline-container--block')
authors_processing = authors.find_all('p')
authors_text = [author.text.replace('\n','').strip() for author in authors_processing]
# authors_text --> list of authors

article_items = [date_clean, category_clean, authors_text, title_clean]

try:
    shutil.copy(src='article_1' +'.joblib', dst='article_1' + '_backup.joblib')
except FileNotFoundError:
    joblib.dump(article_items,'article_1' +'.joblib')
