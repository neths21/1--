from bs4 import BeautifulSoup
from smtplib import SMTP
import requests
import os
my_email=os.getenv("MYEMAIL")
password=os.getenv("MYPASS")
URL="https://appbrewery.github.io/instant_pot/"
response=requests.get(url=URL,headers={"Accept-Language":"en-US" ,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",})
soup=BeautifulSoup(response.text,"html.parser")
data=soup.find(name="span", class_="aok-offscreen")
price=(data.getText()).split("$")[1]
print(price)
if float(price)<120:
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Amazon price aler\n\n HI PRICE AT ${price}\n{URL}")