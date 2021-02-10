valor300plastico=5.10
valor500plastico=9.20
valor300aluminio=10
valor500aluminio=14.50


volume=int(input('Digite o volume: '))
material=str(input('digite o material : ')).upper()
quantidade=int(input('quantidade : '))


if material=='ALUMINIO':
    if quantidade<3 :
        if volume==300:
           print('o valor a ser pago é {}'.format(quantidade*valor300aluminio))
        else:
            print('o valor a ser pago é {}'.format(quantidade*valor500aluminio))
    else:
        if volume==300:
            desconto=(quantidade*valor300aluminio)*10/100
            print('o valor a ser pago é {}'.format(quantidade*valor300aluminio-desconto))
        else:
            desconto=(quantidade*valor300aluminio)*10/100
            print('o valor a ser pago é {}'.format(quantidade*valor300aluminio-desconto))
else:
    if quantidade<=3 :
        if volume==300:
           print('o valor a ser pago é {}'.format(quantidade*valor300plastico))
        else:
            print('o valor a ser pago é {}'.format(quantidade*valor500plastico))
    else:
        if volume==300:
            desconto=(quantidade*valor300plastico)*10/100
            print('o valor a ser pago é {}'.format(quantidade*valor300plastico-desconto))
        else:
            desconto=(quantidade*valor300plastico)*10/100
            print('o valor a ser pago é {}'.format(quantidade*valor300plastico-desconto))
print()


