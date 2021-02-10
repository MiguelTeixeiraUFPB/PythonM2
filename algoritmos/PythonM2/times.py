timea=str(input('digite o nome do time A:'))
timeb=str(input('digite o nome do time B:'))
pontostimea=(int(input('digite a pontuação do time A : ')))
pontostimeb=(int(input('digite a pontuação do time B : ')))
if pontostimea>pontostimeb:
    print('time {} é o vencedor'.format(timea))
elif pontostimea==pontostimeb:
    saldoA=int(input('digite o saldo de gols do time A: '))
    saldoB=int(input('digite o saldo de gols do time B: '))
    if saldoA==saldoB:
         print('Empate')
else:
    print('time {} é vencedor'.format(timeb))
print()