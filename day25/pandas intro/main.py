import pandas
data=pandas.read_csv(r"day25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240727.csv")
c_grey=0
c_cin=0
c_b=0
for i in data["Primary Fur Color"]:
   if i=="Grey":
        c_grey+=1
   elif i=="Cinnamon":
       c_cin+=1
   elif i=="Black":
       c_b+=1
new_data={
   "Fur":["Grey","Red","Black"],
   "Count":[c_grey,c_cin,c_b]
}
new_data=pandas.DataFrame(new_data)
new_data.to_csv("day25\squirrel_count.csv")
#fur colour in primary fir colour count