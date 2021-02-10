import random
computador=random.randint(1,9)
escolha=n2=0
print(computador)
while True:
    escolha=str(input('digite sua escolha: ')).upper()
    n2=int(input('digite um número: '))
    if escolha=='PAR':
        if n2+computador%2==0:
            print('Você venceu')
        else:
            print('você perdeu')
    if escolha=='IMPAR':
        if n2+computador%2!=0:
            print('você venceu')
        else: 
            print('você perdeu')
print()    
