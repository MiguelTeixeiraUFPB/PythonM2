bolas=int(input('digite a quantidade de bolas de sorvete: '))
valorMc=4.50
valorDS=3.80
outros=2.75
if bolas==1:
    sabor=str(input(""" escreva o nome  do sabor escolhido 
[1]Morango
[2]Cereja
[3]Damasco
[4]seriguela
[5]outros sabores
: """)).upper()
    if sabor=='MORANGO' or sabor=='CEREJA':
         print('o sabor escolhido foi {} e o valor é de {}'.format(sabor,valorMc))
    elif sabor=='DAMASCO' or sabor=='SERIGUELA':
        print('o sabor escolhido foi {} e o valor é de {}'.format(sabor,valorDS))
    else:
        print('o sabor escolhido foi {} e o valor é de {}'.format(sabor,outros)) 
elif bolas==2:
    sabor=str(input(""" escreva o nome  do primeiro sabor
    v
[1]Morango
[2]Cereja
[3]Damasco
[4]seriguela
[5]outros sabores
: """)).upper()

    sabor2=str(input(""" escreva o nome  do segundo sabor escolhido 
    v
[1]Morango
[2]Cereja
[3]Damasco
[4]seriguela
[5]outros 
: """)).upper()       
    if sabor=='MORANGO' and sabor2=='MORANGO' or sabor=='MORANGO' and sabor2=='CEREJA' or sabor=='CEREJA' and sabor2=='MORANGO' or sabor=='CEREJA' and sabo2r=='CEREJA':
            print('os sabores escolhido foram {} e {} e o valor é de {}'.format(sabor,sabor2,valorMc*2)) 
    elif sabor=='DAMASCO' and sabor2=='DAMASCO' or sabor=='DAMASCO' and sabor2=='SERIGUELA' or sabor=='SERIGUELA' and sabor2=='DAMASCO' or sabor=='SERIGUELA' and sabor2=='SERIGUELA' :
         print('os sabores escolhido foram {} e {} e o valor é de {}'.format(sabor,sabor2,valorDS*2))
    elif sabor=='MORANGO' and sabor2=='OUTROS' or sabor=='OUTROS' and sabor2=='MORANGO' or sabor=='OUTROS' and sabor2=='CEREJA' or sabor=='CERAJA' and sabo2r=='OUTROS':
        print('os sabores escolhido foram {} e {} e o valor é de {}'.format(sabor,sabor2,outros+valorMc))
    elif sabor=='DAMASCO' and sabor2=='OUTROS' or sabor=='OUTROS' and sabor2=='DAMASCO' or sabor=='SERIGUELA' and sabor2=='OUTROS' or sabor=='OUTROS' and sabor2=='SERIGUELA' :
         print('os sabores escolhido foram {} e {} e o valor é de {}'.format(sabor,sabor2,outros+valorDS))
    else:
         print('os sabores escolhido foram {} e {} e o valor é de {}'.format(sabor,sabor2,outros*2))
elif bolas>2:
    for c in range (sabor)

    print('o número de bolas é {} e o valor é {}'.format)
