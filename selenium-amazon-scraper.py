from urllib.request import urlopen
from bs4 import BeautifulSoup
# selenium is use for automation but in this case, we use it for the scraping the data that have form from the javascript
from selenium import webdriver
from selenium.webdriver.common import by 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# import time
import csv

# url = "http://quotes.toscrape.com/"
# using the driver
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/s?k=bag+pack&rh=p_89%3AKAUKKO&dc&qid=1582619449&rnid=2528832011&ref=sr_nr_p_89_1")

try:
    element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located((by.By.CLASS_NAME, "s-result-item")))
finally:
    # let the time sleep
    # time.sleep(1)
    # get the page info into html 
    html = driver.page_source
    # pass the html page to beautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    quotes = soup.findAll("div", {"class": "s-result-item"})
    # print(quotes[0].find("span", {"class": "a-icon-alt"}).get_text())
    # quotes = soup.findAll("div", {"class": "quote"})

    csvFile = open("bag_pack.csv", "w")
    writer = csv.writer(csvFile)
    writer.writerow(("image_url", "name", "rate", "price"))

    for quote in quotes:
        image_url = quote.find("img").attrs["src"]
        print(quote.find("img").attrs["src"])
        name = quote.find("span", {"class": "a-size-base-plus"}).get_text()
        print(quote.find("span", {"class": "a-size-base-plus"}).get_text())
        # try to get the rate of product
        try:
            rate = quote.find("span", {"class": "a-icon-alt"}).get_text()
            print(quote.find("span", {"class": "a-icon-alt"}).get_text())
        except:
            rate = quote.find("span", {"class": "a-icon-alt"})
            print(quote.find("span", {"class": "a-icon-alt"}))
        # try to get the price of product
        try:
            price = quote.find("span", {"class": "a-offscreen"}).get_text()
            print(quote.find("span", {"class": "a-offscreen"}).get_text())
        except:
            price = quote.find("span", {"class": "a-offscreen"})
            print(quote.find("span", {"class": "a-offscreen"}))
        writer.writerow((image_url, name, rate, rate, price))
            


    csvFile.close()
    driver.close()
    # print(len(quotes))