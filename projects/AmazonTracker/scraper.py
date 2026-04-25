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
    seller_name = soup.find("a", id = "sellerProfileTriggerId")

    # Extract the text from the price element
    price = price_data.getText()

    # Convert the price string to a floating-point number
    # split_price = float(price.split("$")[1])

    # Print the extracted price
    print(product_name)
    print(product_title.getText().strip())
    print(seller_name)
    print(price_data.getText())

    # checking availability
    XPATH_AVAILABILITY = '//div[@id ="availability"]//text()'
    RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
    AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
    #return AVAILABILITY
    return doc

def ReadAsin():
    # Asin Id is the product Id which
    # needs to be provided by the user
    Asin = 'B0B1LF85XW'
    url = "https://www.amazon.com.au/dp/" + Asin
    print ("Processing: "+url)
    ans = check(url)
    arr = [
        'Only 1 left in stock.',
        'Only 2 left in stock.',
        'In stock.']
    print(ans)


