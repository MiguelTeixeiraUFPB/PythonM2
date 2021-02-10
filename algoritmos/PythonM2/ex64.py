numero=0
s=0
c=0
while numero != 999:
    numero=int(input('digite um número: '))
    if numero!=999:
        s=s+numero
        c=c+1
print('fim')
print('a soma dos números é: {} e a quantidade de números digitados é:  {}'.format(s,c))

