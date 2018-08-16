#Author: Angel Octavio Parada Flores
#Fecha: 16/08/18
#Diagrama de flujo par
p=input("Dame un numero ")
S=12
while S!=0:
    if p%2==0:
       p=p+1 
    a=2 
    l=1
    while a < p:
       r=p%a
       if r==0:
          l=0
       break
       a=a+1
    while l!=1:
       p=p+2
    while p<5:
       S=S-p
    else:
       S=S-1
print(p)       
