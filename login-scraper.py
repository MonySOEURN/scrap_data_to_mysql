from urllib.request import urlopen
from bs4 import BeautifulSoup
# selenium is use for automation but in this case, we use it for the scraping the data that have form from the javascript
from selenium import webdriver

driver = webdriver.Chrome()
# go to the web site
driver.get("http://quotes.toscrape.com/js/")

# find and click the login tag
login_element = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/p/a")
login_element.click()

# find the element and insert the value myusername
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys("myusername")

# find the element of password and insert mypassword 
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("mypassword")

# find the submit button element and click
# submit = driver.find_element_by_xpath('/html/body/div/form/input[2]')
submit = driver.find_element_by_xpath('//*[@type="submit"]')
submit.click()

# closing the operations
driver.close()

# *** type of finding xpath: ***
# xpath is the path of the element is node of DOM element 
# ('/html/body/div/form/input[2]') : find the element by using it xpath
# ('//*[@id="password"]'): finding the element using the id tag
# ('//*[@type="password"]'): finding the element using the type of element