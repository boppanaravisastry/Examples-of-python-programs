# prime number  
starting=int(input("enter starting number"))
ending=int(input("enter enging number"))
for i in range(starting,ending+1): 
     if i>1: 
       for n in range(2,i): 
           if (i%n)==0: 
               break
       else: 
            print(i) 
