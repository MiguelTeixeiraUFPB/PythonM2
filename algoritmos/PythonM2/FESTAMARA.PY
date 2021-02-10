import math
qntcookie=20
qntpao=12
custopao=6.79
custocookie=11.34

tipocomida=str(input('digite o tipo de comida: ')).upper()
qntconvidados=int(input('quantidade de convidados: '))

if tipocomida=='COOKIES':
    quantidade=int(math.ceil((qntconvidados/qntcookie)))
    print('o valor a ser pago é {} e a quantidade de sacos é {}'.format(quantidade*custocookie,quantidade))
else:
    quantidade=int(math.ceil((qntconvidados/qntpao)))
    print('o valor a ser pago é {} e a quantidade de sacos é {}'.format(quantidade*custopao,quantidade))
print()


