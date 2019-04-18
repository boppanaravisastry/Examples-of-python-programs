def Fibonacigenerate(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return Fibonacigenerate(a-1)+Fibonacigenerate(a-2)
a=int(input("Enter How Many Times Fibonaci Generate:"))

for i in range(a):
 print(Fibonacigenerate(i),end=",")
