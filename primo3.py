#Author: Angel Octavio Parada Flores
#Fecha: 17/08/18
#1 no es primo
def isPrimefor(num):
    flag=True
    
    if num<2: 
        flag=False
    else:   
     for i in range (2,num-1):
         if num%i==0:
             flag=False
             break 
     return flag

N=input("Dame un numero ")
if not isPrimefor(N):
    print "no es primo"
else: 
    print "es primo"
