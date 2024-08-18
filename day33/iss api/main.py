import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 106.507351 # Your latitude
MY_LONG = -35.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
def isclose():
    if iss_latitude>-60 and iss_latitude<-30:
        if iss_longitude>-155 and iss_longitude<-190:
            return True
    else:
        return False
def isnight():
    if time_now>sunset and time_now<sunrise:
       return True
    else:
        return False
while True:
    time.sleep(60)
    if isclose() and isnight():
        print("yes")
        my_email="example@gmail.com"
        password="fdiy gaum ckkm tpkg"
        with smtplib.SMTP("smptp@gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="Subject:iss\n\n LOOK UP!!!")
# Then send me an email to tell me to look up.
       
# BONUS: run the code every 60 seconds.



