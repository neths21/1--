import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
ch=input("Choose a difficulty. Type 'easy' or 'hard':")
if ch=="easy":
    attempt=10
else:
    attempt=5
num=random.randint(1,100)
while attempt!=0:
    print(f"You have {attempt} attempts remaining to guess the answer")
    guess=int(input("Make a guess: "))
    if guess>num:
        print("Too high")
    elif guess<num:
        print("Too low")
    else:
        print("You win")
        break
    attempt-=1
else:
    if guess!=num:
        print("You lose")