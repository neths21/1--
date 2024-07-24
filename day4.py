import random
print("What do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors.")
a=int(input())
if a==0:
    print('''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"'''
    )
elif a==1:
    print('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
          ''')
elif a==2:
    print('''
           _    (^)
      (_\   |_|
       \_\  |_|
       _\_\,/_|
      (`\(_|`\|
     (`\,)  \ \
      \,)   | |      
        \__(__|
  
          ''')
else:
    print("invalid")
print("Computer chose")
b=random.randint(0,2)
print(b)
if b==0:
    print('''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"'''
    )
elif b==1:
    print('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
          ''')
elif b==2:
    print('''
           _    (^)
      (_\   |_|
       \_\  |_|
       _\_\,/_|
      (`\(_|`\|
     (`\,)  \ \
      \,)   | |      
        \__(__|
  
          ''')
else:
    print("invalid")
if a==0:
    if b==2:
        print("You win")
    else:
        print("You lose")
elif a==1:
    if b==1:
        print("You win")
    else:
        print("You lose")
elif a==2:
    if b==1:
        print("You win")
    else:
        print("You lose")