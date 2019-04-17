num1 = float(input(" Please Enter the First Value : "))
num2 = float(input(" Please Enter the Second Value : "))

i = 1
while(i <= num1 and i <= num2):
    if(num1 % i == 0 and num2 % i == 0):
        gcd = i
    i = i + 1
    
print("\n GCD of {} and {} is {}".format(num1, num2, gcd))
