n=1
par=impar=0
while n!=0:
   n=int(input('digite um número:'))
   if n!=0:
      if n%2==0:
         par+=1
      else:
         impar+=1
print('o número de pares é {} e de impares é {}'.format(par, impar))