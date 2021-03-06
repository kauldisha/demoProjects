from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq




my_url = "https://www.dominos.co.in/great-deals/online-pizza-coupons/everyday-value-offers"
uClient = uReq(my_url)
# read the page data
page = uClient.read()
# close the connection
uClient.close()
# parse all the html code
page_soup = bs(page, "html.parser")

containers = page_soup.findAll("div", {"class": "coupon-contain col-sm-9 col-xs-8"})
print(len(containers))
container = containers[0]


with open("product.csv", "w", encoding="utf-8") as file:

    header = "Pizza Offers"
    file.write(header)
    for container in containers:
        price = container.findAll("span", {"class": "head_text evd-deal_name"})
        prices = price[0].text.strip()
        print(prices)
        file.write("\n")
        file.write(price[0].text.strip())

file.close()