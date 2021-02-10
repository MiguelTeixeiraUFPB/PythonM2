alice=int(input('Alice, digite 0 ou 1: '))
bob=int(input('Bob, digite 0 ou 1: '))
clara=int(input('Clara, digite 0 ou 1: '))

if alice==clara==bob:
    print('empate')
elif alice==clara!=bob:
    print('bob venceu')
elif alice==bob!=clara:
    print('clara venceu')
else:
    print('alice venceu')
print()
