import os
location = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
myfile = open(os.path.join(location,"sample3.txt"),"r+")
myfilenew= open(os.path.join(location,"sample3new.txt"),"w")
a=myfile.readlines()
a1=a
for i in range(len(a)):
    if "a" in a[i]:
        myfilenew.write(a[i])
        a1[i]=""
myfile.seek(0)
open(os.path.join(location,"sample3.txt"),"w").close()
myfile.writelines(a1)
myfile.close()
myfilenew.close()
