# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 13:00:50 2020

@author: Anoushka
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = "https://www.chapters.indigo.ca/en-ca/books/new-this-week/fiction/"
page = requests.get(url)
page_content = page.content 
soup = BeautifulSoup(page_content,'html.parser')
print("***New Fiction Books***")
books = soup.find_all("a", {"class" : "product-list__product-title-link--grid"})
authors = soup.find_all("a", {"class" : "product-list__author-link product-list__contributor"})
for i in range(len(books)) : 
    print(books[i].get_text() + " by " + authors[i].get_text())
    
    