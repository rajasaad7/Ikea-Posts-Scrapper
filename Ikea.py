import requests
from bs4 import BeautifulSoup
import time


def get_source(url):
    header = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    }

    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        category = soup.find("ol", {'class': 'bc-breadcrumb__list'}).text.replace("\n\n\n", "/").replace("\n", "")
    except:
        category = "No on the page"
    try:
        name = soup.find("div", {'class': 'range-revamp-header-section__title--big'}).text
    except:
        name = "No on the page"
    try:
        price = soup.find("span", {'class': 'range-revamp-price__integer'}).text
    except:
        price = "No on the page"
    try:
        description = soup.find("p").text.replace(",", "")
    except:
        description = "No on the page"

    try:
        measurement = soup.find("div", {'class': 'range-revamp-product-dimensions'}).text.replace("Product size",
                                                                                                  "").replace("cm",
                                                                                                              "cm / ")
    except:
        measurement = "No on the page"
    try:
        SKU = soup.find("span", {'class': 'range-revamp-product-identifier__number'}).text
    except:
        SKU = "No on the page"

    final_write = category.replace(",","") + "," + name.replace(",","") + "," + price.replace(",","") + "," + description.replace(",","") + "," + measurement.replace(",","") + "," + SKU + "\n"
    write_to_csv.write(final_write)
    print(final_write)


write_to_csv = open("output1.csv", "w", encoding="utf-8")
write_to_csv.write("Category,Name,Price,Description,Measurement,SKU\n")
links = open("newlinks.txt", "r").readlines()

for link in links:
    get_source(link.strip("\n"))
    time.sleep(3)
