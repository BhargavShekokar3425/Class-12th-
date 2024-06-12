import os
location = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
file1=open(os.path.join(location,"sample17.txt"),"r")
Lines= file1.readlines()
count=1
for line in Lines:
    print("Line{}: {}".format(count, line.strip()))
    count+=1