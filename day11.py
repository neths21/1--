import os
from blackjackart import logo
import random
def disp():
    print(f"Your cards: {myl}, current score: {sum(myl)}")
    print(f"Computer's first card: {cl[0]}")
def user():
    myl.append(random.choice(cards))
def computer():
    score()
    if sum(cl)==21:
        print()
    elif sum(cl)<17:
        cl.append(random.choice(cards))
        print(cl)
def score():
    scu=sum(myl)
    if 11 in myl and sum(myl)>21:
        ind=myl.index(11)
        myl[ind]=1
    scu=sum(cl)
    if 11 in cl and sum(cl)>21:
        ind=cl.index(11)
        cl[ind]=1


def win_lose():
    print(f"Your final hand: {myl}, final score: {sum(myl)}")
    print(f"Computer's final hand: {cl}, Computer's final score: {sum(cl)}")
    if sum(myl)>21:
        print("You went over. You lose	\U0001F62D")
    elif sum(myl)>sum(cl):
        print("You win \U0001F603")
    elif sum(myl)<sum(cl) and sum(cl)>21:
        print("You win \U0001F603")
    elif sum(myl)<sum(cl) and sum(cl)<21:
        print("You lose \U0001F62D")
    else:
        print("Draw \U0001F643")
    return input("Do you want to play a game of Blackjack?Type 'y' or 'n':")

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
ch=input("Do you want to play a game of Blackjack?Type 'y' or 'n':")
while ch=="y":
    myl=[]
    cl=[]
    os.system('cls')
    print(logo)
    myl.append(random.choice(cards))
    myl.append(random.choice(cards))
    cl.append(random.choice(cards))
    cl.append(random.choice(cards))
    disp()
    c=input("Type 'y' to get another card, type 'n' to pass: ")
    while c=="y":
        user()
        score()
        if sum(myl)<21:
            disp()
        else:
            break
        c=input("Type 'y' to get another card, type 'n' to pass: ")
    computer()
    ch=win_lose()