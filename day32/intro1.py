import smtplib
import datetime as dt
import random
#add yoyr gmail
my_email="example@gmail.com"
#differs by service provider
password="fsfy fsdm ckdf tdfg"
now=dt.datetime.now()
print(now.isoweekday()==7)
if now.isoweekday()==7:
    with open(r"day32\quotes.txt") as f1:
        message=random.choice(f1.readlines())
        print(message)
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="example@yahoo.com",
            msg=f"Subject:Motivational quortes\n\n{message}")







