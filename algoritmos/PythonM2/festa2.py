qntpao=12
qntcookies=20
precopao=6.79
precookies=11.34
valor=0
quantidade=0

tipocomida=str(input('digite o tipo de comida :')).upper()
qntpessoas=int(input('digite a quantidade de pessoas que vão à festa:'))

if tipocomida=='COOKIE':
    quantidade=int(qntpessoas/qntcookies)
    print('a quantidade de pacotes é {} e o valor é {}'.format(quantidade,precookies*quantidade))
