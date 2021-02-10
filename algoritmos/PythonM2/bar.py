diaseman=str(input('digite o dia da semana: ')).upper()
feriado=str(input('digite se é feriado ''sim ou não : ')).upper()
segaaquinta=20
sextsab=30
domingo=15

if diaseman=='SEGUNDA' or diaseman=='TERÇA' or diaseman=='QUARTA' or diaseman== 'QUINTA'  :
    if feriado=='NÃO' or feriado=='NAO':
        print('o valo do ingresso a ser pago é {}R$ '.format(segaaquinta))
    else:
        print('o valo do ingresso a ser pago é {}R$ '.format(segaaquinta-(segaaquinta*50/100)))
elif diaseman=='SEXTA' or diaseman=='SÁBADO' or diaseman=='SABADO':
    if feriado=='NÃO' or feriado== 'NAO':
         print('o valo do ingresso a ser pago é {}R$ '.format(sextsab))
    else:
        print('o valo do ingresso a ser pago é {}R$ '.format(sextsab-(sextsab*50/100)))
elif diaseman=='DOMINGO':
    if feriado=='NÃO'or feriado=='NAO':
        print('o valo do ingresso a ser pago é {}R$ '.format(domingo))
    else:
        print('o valo do ingresso a ser pago é {}R$ '.format(sextsab-(sextsab*50/100)))
print()





