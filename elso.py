import random

szamok=[]

#lista feltoltese 100db random 2jegyu egesz szammal
for i in range (100):
    szam=random.randint(10,99)
    szamok.append(szam)
    
#ell
print(len(szamok))
print(szamok) 
