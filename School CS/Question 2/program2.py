import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
myfile = open(os.path.join(location,'sample2.txt'),"r")
vow=con=up=lo=0
b = myfile.read()
for i in b:
    if i.isalpha():
        if i in ["a","e","i","o","u","A","E","I","O","U"]:
            vow += 1
        else:
            con += 1
    if i.isupper():
        up += 1
    else:
        lo += 1

print("no. of vowels = ",vow)
print("no. of consonants = ",con)
print("no. of uppercase letters = ",up)
print("no. of lowercase letters = ",lo)