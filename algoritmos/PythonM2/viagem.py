QuantidadePessoas=int(input('Digite a quantidade de pessoas que vão viajar: '))
viagem=str(input('''Digite [1] se a viagem for para Porto
Digite [2] se a viagem for para pipa:  '''))

valor=float(input('Digite o valor da viagem:'))
valordividido=valor/QuantidadePessoas

print('o valor total é de {:.2f}R$'.format(valor))
if (viagem=='1'):
    print('A viagem será para Porto e cada um pagará {:.2f}R$ '.format(valordividido))
else:
    print('A viagem será para Pipa e cada um pagará {:.2f}'.format(valordividido))
print('Boa viagem')