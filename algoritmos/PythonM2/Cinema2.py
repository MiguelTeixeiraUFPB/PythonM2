SIMPLES=17
COMPLETO=22
FILME2D=10.50
FILME3D=17.50

TipoFilme=str(input('digite o tipo de filme [2D] ou [3D] : ')).upper()
lanche=str(input('deseja comprar lanche? ')).upper()

if lanche=='SIM' and TipoFilme=='2D':
    combo=input('seu combo é simples ou completo: ').upper()
    if combo=='SIMPLES':
        print('o valor a ser pago é {}'.format(SIMPLES+FILME2D))
    elif combo=='COMPLETO':
        print('o valor a ser pago é {}'.format(COMPLETO+FILME2D))
elif lanche=='SIM' and TipoFilme=='3D':
     combo=input('seu combo é simples ou completo: ').upper()
     if combo=='SIMPLES':
        print('o valor a ser pago é {}'.format(SIMPLES+FILME3D))
     elif combo=='COMPLETO':
        print('o valor a ser pago é {}'.format(COMPLETO+FILME3D))
print('Bom filme Professora Ana Liz')

     

       
