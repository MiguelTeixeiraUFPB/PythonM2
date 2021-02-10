TipoFilme=str(input('digite o tipo de filme [2D] ou [3D] : ')).upper()
lanche=str(input('deseja comprar lanche? ')).upper()
if TipoFilme=='2D':
    TipoFilme=int(10.50)
elif TipoFilme== '3D':
    TipoFilme=int(17.50)
    if lanche=='SIM':
        combo=str(input('digite o tipo de combo, simples ou completo: ')).upper()
        if combo=='SIMPLES':
            combo=int(17)
        elif combo=='COMPLETO':
            combo=int(22)
            valor=TipoFilme+combo
        elif TipoFilme== '2D' and combo=='SIMPLES':
             print('o tipo do filme é {} e o valor é {}'.format('2d',valor))