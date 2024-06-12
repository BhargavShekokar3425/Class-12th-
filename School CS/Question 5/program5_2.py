import os
from inspect import modulesbyfile
import pickle
location = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
user = int(input("Enter roll no you want to search: "))
m = int(input("Update the marks: "))
try:
    myfile=open(os.path.join(location,"sample5.dat"),"rb+")
    while True:
        temp=myfile.tell()
        a=pickle.load(myfile)
        if a["rollno"]==user:
            myfile.seek(temp)
            a["Marks"]=m
            pickle.dump(a,myfile)
        print(a)
except FileNotFoundError:
    print("Please check the file name")
except EOFError:
    myfile.close()
    
    