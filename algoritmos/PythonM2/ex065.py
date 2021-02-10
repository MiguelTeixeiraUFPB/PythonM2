n1='s'
n2=0
s=c=0

while n1=='s':
    n2=int(input('digite um número: '))
    n1=str(input(' quer continuar: ')).lower().strip()
    s=n2+s
    c=c+1
    if c==1:
        maior=menor=n2
    else :
        if n2>maior:
            maior=n2
        if n2<menor:
            menor=n2
s=s/c
print('a média obtida é: {}'.format(s))
print(' o maior é {} e o menor é {}'.format(maior,menor))