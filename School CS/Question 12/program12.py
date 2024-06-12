#armstrong
n=int(input("Enter the number to check: "))
n1=n
sum=0
while(n>0):
    ans=n%10;
    sum=sum+(ans**3)
    n=int(n/10)
if sum==n1:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")