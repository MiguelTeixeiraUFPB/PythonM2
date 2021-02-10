passagemAreiaDiurno=19
passagemAreiaNoturno=24
passagemPilarNoturno=26
passagemPilarDiurno=22

destino=str(input('digite o destino: ')).upper()
horario=str(input('digite se o horário é diurno ou noturno: ')).upper()
idade=int(input('digite sua idade: '))

if destino=='AREIA':
    if horario=='DIURNO':
        print('o valor a ser pago é {}'.format(passagemAreiaDiurno))
    else:
        print('o valor a ser pago é {}'.format(passagemAreiaNoturno))
else:
    if horario=='DIURNO':
        if idade==10 or idade==65:
            print('o valor a ser pago é {}'.format(passagemPilarDiurno/2))
        else:
            print('o valor a ser pago é {}'.format(passagemPilarDiurno))
    else:
        if idade==10 or idade==65:
            print('o valor a ser pago é {}'.format(passagemPilarNoturno/2))
        else:
            print('o valor a ser pago é {}'.format(passagemPilarNoturno))
print()



