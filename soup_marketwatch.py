# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:39:15 2022

@author: WIN
"""

# import the html into pyhton
import requests
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/aapl'

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')
soup

# price of the stock

price = soup.find('bg-quote', class_ = 'value').text
price 
# closing price of the stock

close = soup.find('td', class_ = 'table__cell u-semi').text
close

# 52 week range (lower, upper)
nested = soup.find('mw-rangebar',class_ = 'element element--range range--yearly')
nested

lower  = nested.find_all('span', class_ = 'primary')[0].text
lower


upper  = nested.find_all('span', class_ = 'primary')[1].text
upper
 # analysist rating 
 
rating = soup.find('li', class_ = 'analyst__option active').text
rating 
