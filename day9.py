import os
ch="yes"
d={}
while ch=="yes":
    na=input(("What is your name? "))
    bd=int(input("Whats your bid:$ "))
    d[na]=bd
    print("Are there any other bidders?type yes or no")
    ch=input()
    os.system('cls')
m=-1
for i in d:
    if d[i]>m:
        m=d[i]
        ind=i
print(f"the winner is {i} with a bid of {m}")