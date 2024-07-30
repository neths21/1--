with open(r"day24\Input\Names\invited_names.txt") as f1:
    l=f1.readlines()
for i in l:
    name=i.strip()
    print(name)
    with open(r"D:\code\python\100 days of python\day24\Input\Letters\starting_letter.txt")as f2:
        data=f2.read()
        data1=data.replace("[name]",name)
        print(data1)
    with open(f"D:\\code\\python\\100 days of python\day24\Output\ReadyToSend\Letter_for_{name}.txt","w") as f3:
        f3.write(data1)