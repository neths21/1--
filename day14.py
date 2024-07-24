from gamedata import data
from gameart import logo,vs
import os
import random
score=0
A=random.choice(data)
print(logo)
while True:
    B=random.choice(data)
    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}, {A['follower_count']}")
    print(vs)
    print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]},{B['follower_count']}")
    ch=input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if A['follower_count']>B['follower_count']:
        ma="A"
    else:
        ma="B"
    if ch==ma:
        score+=1
        A=B
        os.system('cls')
        print(logo)
        print(f"You're right! Current score: {score}")
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry. that's wrong.Final score: {score}")
        break
