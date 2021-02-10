from random import randint

itens=('pedra','papel','tesoura')
computador=randint(0,2)

opcao=int(input('digite sua opção: '))
print('=x'*15)
print('o computador escolheu {}'.format(itens[computador]))
print('você escolheu {}'.format(itens[opcao]))
print('=x'*15)

if computador==0 and opcao==2:
    print('você perdeu')
elif computador==0 and opcao==1:
    print('você ganhou')
elif computador==0 and opcao==0 :
    print('empatou')
elif computador==1 and opcao==0:
    print('você perdeu')
elif computador==1 and opcao==1:
    print('empatou')
elif computador==1 and opcao==2:
    print('você ganhou')
elif computador==2 and opcao==0:
    print('você ganhou')
elif computador==2 and opcao==1:
    print('você perdeu')
else:
    print('empatou')
print()
    

