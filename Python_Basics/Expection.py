car={}
model = ["BMW","BENZ","Merc"]
features = [[1995,1.0,2000],[1998,2.0,201],[1997,3.0,2002]]

for i in model:
    for j in features:
        car[i]=j
print(car)

try:
    print(car['color'])
except:
    print("there was no key called color")


finally:
    print("it was wxecuted")

#my_file=open("first_file.txt","r+")

for i in car:
    print(car[i])

