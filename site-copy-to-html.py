from urllib.request import urlopen
from bs4 import BeautifulSoup

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
def crawl_url(pageUrl):
    url = "http://books.toscrape.com/" + pageUrl
    # url = pageUrl
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    try:
        try:
            new_url = soup.find("li", {"class": "next"})
            print("-----" + new_url.a.attrs['href'])
            catalogue_str = "catalogue/"
            # condition to check if the next page have catalogue index or not
            if catalogue_str in new_url.a.attrs['href']:
                htmlFile = open(new_url.a.attrs['href'], 'w')
                # using recursive algorithms to crawl
                crawl_url(new_url.a.attrs['href'])
            else:
                htmlFile = open(catalogue_str + new_url.a.attrs['href'], 'w')
                # using recursive algorithms to crawl with index of catalogue
                crawl_url(catalogue_str + new_url.a.attrs['href'])
            htmlFile.write(str(soup))
            htmlFile.close()
        except AttributeError as e:
            print("Crawling finished")
            return None
    finally:
        return None

crawl_url("")

