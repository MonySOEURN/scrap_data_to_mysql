from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

#convert word number to integer
def word2num(word):
    print(word.lower())
    lWord = word.lower()
    if lWord == "one":
        return 1
    elif lWord == "two" :
        return 2
    elif lWord == "three" :
        return 3
    elif lWord == "four":
        return 4
    else:
        return 5
    
# grab each product
books = soup.findAll("article", {"class": "product_pod"})
# print(books[0].p.attrs["class"][1])
csvFile = open("books.csv", "w")

try:
    write = csv.writer(csvFile)
    write.writerow(("Title", "URL", "Price", "Rate", "Availability"))
    for book in books:
        title = book.h3.a.attrs["title"]
        book_url = book.a.attrs["href"]
        price = book.find("p", {"class": "price_color"}).get_text()
        rate = word2num(book.p.attrs["class"][1])
        availability = book.find("p", {"class": "instock availability"}).get_text().strip()
        # print(books[0].h3.a.attrs["title"])
        # print(books[0].find("p", {"class": "price_color"}).get_text())
        # print(books[0].find("p", {"class": "instock availability"}).get_text().strip())
        write.writerow((title, url + book_url, price, rate, availability))
        # print(title)
        # print(price)
        # print(availability)
finally:
    csvFile.close()