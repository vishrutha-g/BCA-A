#A binary operation * is defined on the set Z={0,1,2,3,4,5,6,7,8,9,10} by a*b=1+ab for all a,b in Z.
#Show that * is comutative but not associative.

import sys as s
#set of Z
Z={0,1,2,3,4,5,67,8,9,10}

#Defining the function 
def f(a,b):
    return(1+(a*b))

#Commutative Law
flag=1 #consider commutative
for a in Z:
        for b in Z:
                if f(a,b)!=f(b,a):  #if a*b is not equal to b*a
                        flag=0
if flag!=0:
    print("The binary operation * in Z is commutative")
else:
    print("The binary operation * in Z is not commutative")
    s.exit()


#Associative Law
flag1=1 #consider Associative   
for a in Z:
        for b in Z:
            for c in Z:
                if f(a,f(b,c))!=f(f(a,b),c):  #if a*(b*c) is not equal to a*(b*c)
                    flag1=0
if flag1!=0:
   print("The binary operation * in  is Associative")
else:
   print("The binary operation * in Z is not Associative")
   s.exit()                    
                    
                        