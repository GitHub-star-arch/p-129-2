from cmath import inf
import csv

df=[]
df1=[]
with open('dwarfstars.csv','r') as f:
    r = csv.reader(f)
    for i in r:
        df.append(i)
headers = df[0]
star_data = df[1:]
for i in star_data:
    df=df[df['radius'].notna()]
star_data.sort(key=lambda star_data:star_data[2])
with open('dwarfstars_2.csv','a+') as f:
    w = csv.writer(f)
    w.writerow(headers)
    w.writerows(star_data)

with open('dwarfstars_2.csv','r') as f:
    r = csv.reader(f)
    for i in r:
        df1.append(i)
headers = df1[0]
star_data = df1[1:]
for i in star_data:
    df1=df1[df1['mass'].notna()]
star_data.sort(key=lambda star_data:star_data[2])
with open('dwarfstars_3.csv','a+') as f:
    w = csv.writer(f)
    w.writerow(headers)
    w.writerows(star_data)