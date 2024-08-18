import requests
import datetime as dt
import smtplib
parameters={"lat":13.081527,"lng":80.282146,"formatted":0}
response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status
data=response.json()
sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
now=int(dt.datetime.now())
print(sunrise)
print(sunset)
print(now.hour)
