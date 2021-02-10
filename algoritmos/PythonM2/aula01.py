#estrutura condicional aninhada
ValorCasa=float(input('digite o valor da casa: '))
Salario=float(input('digite o valor do salário mensal : '))
TempoPagamento=int(input('digite o tempo em anos: '))
TempoPagamento=TempoPagamento*12
prestacao=ValorCasa/TempoPagamento
print('para pegar uma casa de {:.2f} em {} anos o valor da prestação é de {:.2f} '.format(ValorCasa,TempoPagamento/12,prestacao))
if prestacao<= Salario*30//100: 
    print('a prestação será de {:.2f} por {:.2f} anos'.format(prestacao,TempoPagamento/12))
else:
    print('você não pode financiar essa casa')
    
