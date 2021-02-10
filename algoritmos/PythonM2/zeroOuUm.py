alice=int(input('digite a escolha de Alice 0 ou 1: '))
bob=int(input('digite a escolha de Bob0 ou 1: '))
clara=int(input('digite a escolha de clara 0 ou 1: '))
if alice==bob and bob==clara:
    print('o jogo seu empate, todos colocaram {}'.format(alice))
elif alice>bob and bob==clara :
    print('o vencedor é alice')
elif bob>alice and alice==clara:
    print('o vencedor é bob')
elif clara>bob and alice==bob:
    print('a vencedora é clara')
else: 
    print('o vencedor é ')