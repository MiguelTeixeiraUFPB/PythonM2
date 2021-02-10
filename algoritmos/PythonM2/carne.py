kgcarne=float(input('digite a quantidade de kg de carnes: '))
tipocarne=str(input('digite o tipo de carne : ')).upper
pm=40 
cc=30
outras=25
valorpc=kgcarne*pm
valorcc=kgcarne*cc
valoroutras=kgcarne*outras
if tipocarne=='PICANHA' or tipocarne=='MAMINHA':
    if valorpc>50:
        print('recebe 1kg de linguiça')
    print(' o valor é {}'.format(kgcarne*pc)
elif tipocarne=='CUPIM' or tipocarne=='COSTELA':
    print('o valor é {} '.format(kgcarne*cc))
    if valorcc>50:
        print('recebe 1kg de linguiça')
else:
    print('o valor é {}'.format(kgcarne*outras))
    if valorcc>50:
        print('recebe 1kg de linguiça')
