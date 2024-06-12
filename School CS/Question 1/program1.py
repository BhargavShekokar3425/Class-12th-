import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
myfile = open(os.path.join(location,'sample1.txt'),"r")
a = myfile.readlines()
for i in range(len(a)):
    b = a[i].split()
    print("#".join(b))
myfile.close