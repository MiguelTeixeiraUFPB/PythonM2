taxa=12
diaria=90
carro=str(input('Deseja alugar carro: ')).upper()
if carro=='SIM':
    dias=int(input('digite a quantidade de dias que pretende ficar com o carro: '))
    km=int(input('digite o tamanho da viagem q deseja fazer: '))
    media=km//dias
    if media<=100:
        print('o valor a ser pago é {:.2f}R$'.format(dias*diaria))
    else: 
        diferenca=media-100
        print('o valor a ser pago é {:.2f}R$'.format(dias*diaria+diferenca*12))
else:
    print('você não deseja aluga rum carro')
