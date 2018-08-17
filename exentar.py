#Author: Angel Octavio Parada Flores
#Fecha: 16/08/18
#Diagrama de flujo par
p=input("Dame un numero ")
S=12
a=2
l=1
while S!=0:
     if p%2==0:
        p=p+1
     while l==0:
        p=p+2
     while a < p:
        r=p%a
        if r==0:
           l=0
        a=a+1
     if p<S:
        S=S-p
     else:
        S=S-1
     p=p+2
print(p)       
