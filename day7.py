import random
import hangmanart as hga,hangmanwords as hgw
co=0
c=0
wrong=0
print(hga.logo)
chosen_word=random.choice(hgw.word_list)
l=["_"for _ in range(len(chosen_word))]
print(l)
print("Guess a letter")
while "_" in l:
    
    a=input().lower()
    if a in l:
        print("ALREADY")
        continue
    for i in range(len(chosen_word)):
        if a==chosen_word[i]:
            l[i]=a
            c+=1

    else:
        if c==0:
            wrong-=1
            print(hga.stages[wrong])
    print(l)
    c=0
    if wrong==-7:
        print("you lose")
        break
else:
    if wrong==-7:
        print("you lose")
    else:
        print("You win")