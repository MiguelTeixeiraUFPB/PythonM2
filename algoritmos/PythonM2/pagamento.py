valor=float(input('digite o valor a ser pago pelo produto: '))
parcelas=int(input('quantidade de parcelas: '))
pagamento=str(input('digite [1] para pagamento em dinheiro, [2] para pagamento em cartão e [3] em cheque: '))

juros=(valor*20)/100
desconto10=valor*10/100
desconto5=valor*5/100

if parcelas<=1 and pagamento=='1' :
    valor=valor-desconto10
    print('o valor com desconto de 10% é de {:.1f}'.format(valor))
elif parcelas<=1 and pagamento=='2':
    valor=valor-desconto10
    print('o valor com desconto de 10% é de {:.1f}'.format(valor))
elif parcelas<=1 and pagamento=='2':
    print('o valor no cartão com desconto de 5% é de {:.1f}'.format(desconto5))
elif parcelas<=2 and pagamento=='2':
    print('o valor a ser pago é {:.1f}'.format(valor))
elif parcelas>=3 and pagamento=='2':
    print('o juros a ser pago é de 20% e o valor final é de {:.1f} '.format(valor+juros))