n1 = int(input("Enter any number: "))
sum = 0
for i in range(1, n1):
    if(n1 % i == 0):
       sum = sum + i
if (sum == n1):
    print(n1,'is a Perfect number!')
else:
    print(n1, 'is not a Perfect number!')
