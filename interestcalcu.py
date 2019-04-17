#Interest Calculator
principal=float(input("Money Currently:"))
rate=float(input("Interest rate?:"))
time=int(input("years interest compounded?:"))
print('Interest = ',((principal*time*rate)/100))
