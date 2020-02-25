from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


#convert word number to integer
def word2num(word):
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

# method to get the data from the website
def crawl_url(pageUrl, writer):
    url = "http://books.toscrape.com/" + pageUrl
    # url = pageUrl
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.prettify())
        
    # grab each product
    books = soup.findAll("article", {"class": "product_pod"})
    # print(books[0].p.attrs["class"][1])

    try:
        for book in books:
            title = book.h3.a.attrs["title"]
            book_url = book.a.attrs["href"]
            price = book.find("p", {"class": "price_color"}).get_text()
            rate = word2num(book.p.attrs["class"][1])
            availability = book.find("p", {"class": "instock availability"}).get_text().strip()
            # print(books[0].h3.a.attrs["title"])
            # print(books[0].find("p", {"class": "price_color"}).get_text())
            # print(books[0].find("p", {"class": "instock availability"}).get_text().strip())
            writer.writerow((title, url + book_url, price, rate, availability))
            # print(title)
            # print(price)
            # print(availability)
        try:
            new_url = soup.find("li", {"class": "next"})
            print("-----" + new_url.a.attrs['href'])
            catalogue_str = "catalogue/"
            # condition to check if the next page have catalogue index or not
            if catalogue_str in new_url.a.attrs['href']:
                # using recursive algorithms to crawl
                crawl_url(new_url.a.attrs['href'], writer)
            else:
                # using recursive algorithms to crawl with index of catalogue
                crawl_url(catalogue_str + new_url.a.attrs['href'], writer)
        except AttributeError as e:
            print("Crawling finished")
            return None
    finally:
        csvFile.close()


csvFile = open("books.csv", "w")
writer = csv.writer(csvFile)
writer.writerow(("Title", "URL", "Price", "Rate", "Availability"))
crawl_url("", writer)

