nome1=str(input('digite o nome do 1º vendedor: '))
nome2=str(input('digite o nome do 2º vendedor: '))
total1=float(input('digite o total de vendas de {} é: '.format(nome1)))
total2=float(input('digite o total de vendas de  {} é: '.format(nome2)))

bonus1=total1*5//100
bonus2=total2*5//100 

if total1>total2:
    print('o vendedor que mais vendeu é {} e o valor de seu bonús é {}'.format(nome1,bonus1))
elif total1==total2:
    print('os dois venderam o mesmo tanto')
else:
     print('o vendedor que mais vendeu é {} e o valor de seu bonús é {}'.format(nome2,bonus2))
print('fim')