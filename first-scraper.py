from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser"
# print(soup.prettify())

# grab each product
books = soup.findAll("article", {"class": "product_pod"})

for book in books:
    title = book.h3.a.attrs["title"]
    price = book.find("p", {"class": "price_color"}).get_text()
    availability = book.find("p", {"class": "instock availability"}).get_text().strip()
    # print(books[0].h3.a.attrs["title"])
    # print(books[0].find("p", {"class": "price_color"}).get_text())
    # print(books[0].find("p", {"class": "instock availability"}).get_text().strip())
    print(title)
    print(price)
    print(availability)