from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import csv
my_url= "https://www.dominos.co.in/great-deals/online-pizza-coupons/everyday-value-offers"
uClient= uReq(my_url)
#read the page data
page=uClient.read()
#close the connection
uClient.close()
#parse all the html code
page_soup= bs(page,"html.parser")
containers= page_soup.findAll("div",{"class": "coupon-contain col-sm-9 col-xs-8"})
print(len(containers))
container= containers[0]
#prize= container.findAll("span",{"class":"head_text evd-deal_name"})
#created a file'product' and open that file in write mode
filename= "product2.csv"
with open('filename','w',encoding="utf-8") as f:
    header="prod\n"
    f.write(header)
    for container in containers:
        prize= container.findAll("span",{"class":"head_text evd-deal_name"})
        prizes= prize[0].text.strip()
        print(prizes)
        f.write(prize[0].text.strip())
f.close()
