from urllib.request import urlopen
from bs4 import BeautifulSoup
# selenium is use for automation but in this case, we use it for the scraping the data that have form from the javascript
from selenium import webdriver
import time

# url = "http://quotes.toscrape.com/"
# using the driver
driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/js/")
# let the time sleep
time.sleep(1)
# get the page info
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

quotes = soup.findAll("div", {"class": "quote"})
# quotes = soup.findAll("div", {"class": "quote"})
for quote in quotes:
    print(quote.find("span", {"class": "text"}).get_text())
    
driver.close()
# print(len(quotes))