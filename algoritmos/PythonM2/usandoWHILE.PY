n=1
par=0
impar=0
while n!=0:
    n=int(input('digite um número: '))#enquanto o n for diferente de 0 ele vai repetir esse input
    if n%2==0:
        par+=1
    else:
        impar+=1
print('o número de pares é {}'.format(par))
print('o número de impaes é {}'.format(impar))