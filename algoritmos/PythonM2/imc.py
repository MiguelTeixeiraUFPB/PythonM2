peso=float(input('digite seu peso: (Kg)'))
altura=float(input('digite sua altura: (m)'))
imc=peso/(altura**2)
print('o imc da pessoa é de {:.1f}'.format(imc))
if imc<18.5:
    print('você está abaixo do peso')
elif imc>=18.5 and imc<25:
    print('você está no peso ideal')
elif imc>25 and imc<30:
    print(' sobrepeso')
else:
    print('você está em obesidade')