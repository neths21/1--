import random
pa=""
pa1="21"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
a=int(input("How many letters would you like in your password?\n"))
b=int(input("How many symbols would you like?\n"))
c=int(input("How many numbers would you like?"))
for i in range(0,a):
    r1=random.randint(0,len(letters)-1)
    pa=pa+letters[r1]
for i in range(0,b):
    r1=random.randint(0,len(numbers)-1)
    pa=pa+numbers[r1]
for i in range(0,a):
    r1=random.randint(0,len(symbols)-1)
    pa=pa+symbols[r1]
print("Here is your password:",pa)
pa=list(pa)
random.shuffle(pa)
pas=""
for i in pa:
    pas+=i
print("Here is your password:",pas)
