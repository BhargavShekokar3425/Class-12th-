import os
location = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
fh=open(os.path.join(location,"sample24.txt",),"r")
item=[] 
a=""
while True:
    a=fh.readline() 
    words=a.split() 
    for j in words:
        item.append(j)
    if a =="": break
print("#".join(item))