largura=float(input('digite a largura da sua mala em (cm) : '))
altura=float(input('digite a altura da sua mala em (cm) : '))
comprimento=float(input('digite o comprimento da sua mala em (cm): '))

if largura<=45 and altura<=56 and comprimento<=25:
    print('sua bagagem está dentro do padrão, Boa viagem.')
else:
    print('sua bagagem está fora do padrão permitido pela compania e não foi aceita.')
print()