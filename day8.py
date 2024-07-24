con="yes"
while con=="yes":
    print("Type 'encode' to encrypt, type 'decode' to descrypt:")
    ch=input().lower()
    print("Typer your message:")
    mes=input()
    print("Type your shift number")
    num=int(input())
    res=""
    if ch=="encode":
        for i in mes:
            if i.isalpha():
                res=res+chr(ord(i)+num)
            else:
                res=res+i
    elif ch=="decode":
        for i in mes:
            if i.isalpha():
                res=res+chr(ord(i)-num)
            else:
                res=res+i
    print(f"Here's the encoded result: {res}")
    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    con=input()