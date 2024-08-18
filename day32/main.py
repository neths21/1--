import smtplib
import random
import pandas
import datetime as dt


def check_bday():
    df=pandas.read_csv(r"day32\birthdays.csv")
    df=pandas.DataFrame(df)
    print(df)
    for i in range(len(df)):
        if df["month"].iloc[i]==now.month and df["day"].iloc[i]==now.day:
            name=df["name"].iloc[i]
            send_email(name)
def send_email(name):
    my_email="example@gmail.com"
    #differs by service provider
    password="bfbg gfdm ckom tgkg"
    letters=["day32\letter_templates\letter_1.txt","day32\letter_templates\letter_2.txt","day32\letter_templates\letter_3.txt"]
    with open(random.choice(letters)) as f1:
        bdaywish=f1.read()
        bdaywish=bdaywish.replace("[NAME]",name)
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="example@yahoo.com",msg=f"Subject:Happy birthday\n\n{bdaywish}")
now=dt.datetime.now()
check_bday()
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
