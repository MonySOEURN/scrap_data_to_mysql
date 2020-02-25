from urllib.request import urlopen
from bs4 import BeautifulSoup
import mysql.connector

# connect to the database
cnx = mysql.connector.connect(
    user = 'root',
    password = 'root',
    host = 'localhost',
    database = 'python_scraping',
    unix_socket = '/Applications/MAMP/tmp/mysql/mysql.sock',
    port=3306,
)

cursor = cnx.cursor()

sql = "INSERT INTO `books` (`title`, `book_url`, `price`, `rate`, `availability`) VALUES ( %s, %s, %s, %s, %s )"

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
def crawl_url(pageUrl, book_arr):
    main_url = "http://books.toscrape.com/"
    url = main_url + pageUrl
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

            # writer.writerow((title, url + book_url, price, rate, availability))
            book_arr.append((title, main_url + book_url, price, rate, availability))
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
                crawl_url(new_url.a.attrs['href'], book_arr)
            else:
                # using recursive algorithms to crawl with index of catalogue
                crawl_url(catalogue_str + new_url.a.attrs['href'], book_arr)
        except AttributeError as e:
            print("Crawling finished")
            return book_arr
    finally:
        return book_arr

book_arr = crawl_url("", [])
cursor.executemany(sql, book_arr)
cnx.commit()
cursor.close()
cnx.close()
print("Database insert Finished")
