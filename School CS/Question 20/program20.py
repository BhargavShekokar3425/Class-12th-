import os
location = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
import pickle
import sys
dict={}
#Function to write
def write_in_file():
    file=open(os.path.join(location,"stud2.dat"),"ab")#a-append, b-binary
    no=int(input("Enter the number of students: "))
    for i in range(no):
        print("Enter the details of student ",i+1)
        dict["roll"]=int(input("Enter roll number: "))
        dict["name"]=str(input("Enter name: "))
        dict["marks"]=int(input("Enter marks: "))
        pickle.dump(dict,file)#dump-to write in student file
    file.close()
#function to display
def display():
#read from the file and display]
    file=open(os.path.join(location,"stud2.dat"),"rb")
    try:
        while True:
                stud=pickle.load(file)#write to the file
                print(stud)
    except EOFError:
        pass
    file.close()
#function to display
def search():
    file=open("stud2.dat","rb")#r-read, b-binary
    r=int(input("Enter the rollno to search: "))
    found=0
    try:
        while True:
            data=pickle.load(file)#read from file
            if data["roll"]==r:
                print("The rollno= ",r," record found")
                print(data)
                found=1
                break
    except EOFError:
        pass
    if found==0:
        print("The roll no= ",r," record not found")
    file.close()
#Main program
while True:
    print("Menu \n 1-write in a file \n 2-display")
    print(" 3-search \n 4-exit\n")
    ch=int(input("Enter your choice= "))
    if ch==1:
        write_in_file()
    if ch==2:
        display()
    if ch==3:
        search()
    if ch==4:
        print("Hari Om")
        sys.exit()
