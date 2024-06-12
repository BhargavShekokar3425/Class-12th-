import pickle
import os 
location = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
myfile = open(os.path.join(location,"sample4.dat"),"wb+")
a={}
found=False
for i in range(5):
    roll=int(input("enter the roll num: "))
    name=input("enter the name: ")
    a["roll"]=roll
    a["name"]=name
    pickle.dump(a,myfile)

myfile.seek(0)
c=int(input("enter the roll no to search: "))
try:
    while True:
        b=pickle.load(myfile)
        if b["roll"]==c:
            print(b)
            found=True
except EOFError:
    if found:
        myfile.close()
    else:
        print("student detalls not found")
        myfile.close()