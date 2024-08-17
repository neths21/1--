import pandas
nato={}
data=pandas.read_csv(r"day26\nato_phonetic_alphabet.csv")
data=pandas.DataFrame(data)
#nato=[row.letter:row.code for (index,row)in data.iterrows() ]
for (index,row)in data.iterrows():
    nato[row.letter]=row.code
print(nato)
def generate():
    a=input("enter name").upper()
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    try:
        l=[nato[i] for i in a]
    except KeyError:
        print("Wrong input")
        generate()
    else:
        print(l)
generate()