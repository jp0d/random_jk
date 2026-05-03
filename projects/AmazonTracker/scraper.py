# importing libraries
from lxml import html
import requests
from bs4 import BeautifulSoup
from time import sleep
import time
import schedule
import smtplib


def check(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}

    # adding headers to show that you are
    # a browser who is sending GET request
    page = requests.get(url, headers=headers)
    # parsing the html content
    doc = html.fromstring(page.content)

    print(page)

    # Parse the HTML content of the page
    soup = BeautifulSoup(page.content, "lxml")

    # Find the element that contains the price
    price_data = soup.find("span", class_="a-price-whole")
    product_name = soup.find("span", class_="a-size-large product-title-word-break")
    product_title = soup.find("span", id="productTitle")
    product_rating = soup.find('span', {'data-hook': 'rating-out-of-text'}).get_text(strip=True)
    seller_name = soup.find("a", id = "sellerProfileTriggerId")

    # Extract the text from the price element
    price = price_data.getText()

    # Print the extracted price
    # print(product_name)
    # print(product_title.getText().strip())
    # print(seller_name)
    # print(product_rating)
    # print(price_data.getText())

    prod_info = {'product_title': product_title.getText().strip(),
                 'seller_name': seller_name,
                 'product_rating': product_rating,
                 'price': price,
                 'product_url': url
                 }

    return prod_info

def readAsin(amazon_url, asin_id):
    # Asin Id is the product Id which
    # needs to be provided by the user
    url = amazon_url + asin_id
    print ("Processing: "+url)
    ans = check(url)
    return(ans)


