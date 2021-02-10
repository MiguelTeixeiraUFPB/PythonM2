n1=0

while True:
    n1=int(input('digite um número para obter a tabuada: '))
    for c in range(1,11):
        print('-'*30)
        print('{} x {} = {}'.format(n1,c,n1*c))
    if n1<0:
        break
print('fim')