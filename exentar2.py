#Author: Angel Octavio Parada Flores
#Fecha: 17/08/18
#Diagrama de flujo par
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

p=input("Dame un numero ")
S=12
while S!=0:
     if p%2==0:
        p=p+1
     while not IsPrimefor(p):
        p=p+2
        if p%2==0:
           p=p+1
     while p<S:
        S=S-p
     else:
        S=S-1
     p=p+2
print(p)

