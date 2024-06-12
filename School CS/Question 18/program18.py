import os
location = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
file1=open(os.path.join(location,"sample18.txt",),"r")
file2=open(os.path.join(location,"sample18new.txt"),"w")

for line in file1:
    if "a" in line:
        line=line.replace("a"," ")
    else:
        file2.write(line)
file1.close()
file2.close()
print ("Changes have been made")