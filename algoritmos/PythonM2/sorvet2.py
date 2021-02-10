bolas=int(input('digite o número de bolas: '))
if bolas<=2:
    print('você não tem direito a calda')
    saborm=int(input('quantas bolas de morango ou cereja você deseja: '))
    sabord=int(input('quantas bolas de damasco ou seriguela você deseja: '))
    outros=int(input('quantas bolas de outro sabor você deseja: '))
    valorm=4.50*saborm
    valord=3.80*sabord
    valoroutros=2.75*outros
    valorfinal= valord+valorm+valoroutros
    print(' valor = {}'.format(valorfinal))
elif bolas>2:
    print('você tem direito a calda')
    saborm=int(input('quantas bolas de morango ou cereja você deseja: '))
    sabord=int(input('quantas bolas de damasco ou seriguela você deseja: '))
    outros=int(input('quantas bolas de outro sabor você deseja: '))
    valorm=4.50*saborm
    valord=3.80*sabord
    valoroutros=2.75*outros
    valorfinal= valord+valorm+valoroutros
    print(' valor = {}'.format(valorfinal))