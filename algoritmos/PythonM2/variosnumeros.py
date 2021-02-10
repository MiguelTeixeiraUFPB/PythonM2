n1=0
c=0
while n1!=99:
    n1=int(input('digite um número para parar: '))
    n1=n1+n1
    c=c+1
print('você digitou {} números'.format(c))