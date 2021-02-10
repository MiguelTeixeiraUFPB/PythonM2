n1=s=c=0
while True:
    n1=int(input('digite um número ou (999) para parar '))
    if n1==999:
        break
    c=c+1
    s=n1+s
print('a quantidade de números digitados é {} e a soma é {} '.format(c,s))