n = int(input('Enter any number: '))
sum1 = 0
for i in range (1,n):
    if (n % i == 0):
        sum1 +=i
if (sum1 == n):
    print("The number ",n," is a perfect number")
else:
    print("The number ",n," is not a perfect number ")
