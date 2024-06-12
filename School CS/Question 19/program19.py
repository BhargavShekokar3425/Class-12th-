import os
location = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
file1=open(os.path.join(location,"sample19.txt",),"r")
vowels=0
consonants=0
uppercase=0
lowercase=0
str1=file1.read()
for i in str1:
    if(i>="a" and i<= "z"):
        lowercase +=1
    elif(i>="A" and i<="Z"):
        uppercase +=1
for j in str1:
    j=j.lower()
    if(j=="a" or j=="e" or j=="i" or j=="o" or j=="u"):
        vowels+=1
    
    else:
        if j.isalpha():
            consonants+=1
print("lower case count: ",lowercase)
print("upper case count: ",uppercase)
print("vowels count: ",vowels)
print("consonants count: ",consonants)

