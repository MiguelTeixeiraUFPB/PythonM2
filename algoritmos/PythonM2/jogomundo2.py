n1=int(input('digite o primeiro número: '))
n2=int(input('digite o segundo número: '))

opcao=1
while not opcao== 5:
    opcao=int(input('''digite uma opção
    [1] soma
    [2]multiplicação
    [3]divisão
    [4] maior
    [5] finalizar
    :'''))
    if opcao==1:
        print('a soma é ',n1+n2)
    elif opcao==2:
        print(n1*n2)
    elif opcao==3:
        print(n1/n2)
    elif opcao==4:
        if n1>n2:
            print('o maior é',n1)
        else:
            print('o maior é',n2)
print('fim')