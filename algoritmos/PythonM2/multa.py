localproibidoCalcada=430
localproibidofaixa=580
velocidademulta=70
falarnocel=830

tipodeinfracao=str(input('TIPO DE INFRAÇÃO: (calçada),(faixa),(celular)? ')).upper()
velocidade=int(input('velocidade: '))

if tipodeinfracao=='CALÇADA':
    print('o valor a ser pago é {}R$ por estacionar na calçada'.format(localproibidoCalcada))
elif tipodeinfracao=='FAIXA':
    print('o valor a ser pago é {}R$ por estacionar em faixa de pedestre'.format(localproibidofaixa))
else:
    print('o valor a ser pago é {}R$ pela multa de falar no celular'.format(falarnocel))
print()
if velocidade>50:
    velocidade=(velocidade-50)*70
    print('Você ultrapassou o limite de velocidade, o valor a ser pago é {}R$'.format(velocidade))
print('fim ')