from urllib.request import urlopen
from bs4 import BeautifulSoup
# selenium is use for automation but in this case, we use it for the scraping the data that have form from the javascript
from selenium import webdriver
from selenium.webdriver.common import by 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# import time

# url = "http://quotes.toscrape.com/"
# using the driver
driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/js/")

try:
    element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located((by.By.CLASS_NAME, "quote")))
finally:
    # let the time sleep
    # time.sleep(1)
    # get the page info into html 
    html = driver.page_source
    # pass the html page to beautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    quotes = soup.findAll("div", {"class": "quote"})
    # quotes = soup.findAll("div", {"class": "quote"})
    for quote in quotes:
        print(quote.find("span", {"class": "text"}).get_text())
        
    driver.close()
    # print(len(quotes))