from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver = webdriver.Firefox()

products=[] #List to store name of the product

count = 0
while count < 100:
    count+=1
    line = "https://pinda.in/cities/mumbai-maharashtra?page="+str(count)
    driver.get(line)


    content = driver.page_source
    soup = BeautifulSoup(content,"html.parser")
    for a in soup.findAll('div', attrs={'class':'adrsitem'}):

        name=a.find('li')

        products.append(name.text)

files = open(r'D:\Documents\codes\Data Science\News Category\nd.txt', 'a')
print(products, file=files)
files.close()