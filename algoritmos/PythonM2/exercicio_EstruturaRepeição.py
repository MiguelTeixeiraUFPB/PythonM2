#comando for uma estrutura de repetição : laço c no intervalo (0,6)
for c in range(0,6):
    print('oi')
print('fim')

#contagem
for c in range(0,6): # se colocar de 0 a 6 ele contara até 5, nesse caso colocamos até 7 para contar até 6
    print(c)
print('fim')

#contagem regressiva
for c in range(6,0,-1):
    print(c)
print('fim')

#contagem pulando de 2 em 2
for c in range(0,7,2):
    print(c)
print('fim')

#contagem com input
num=int(input('digite um número: '))
for c in range(0,num+1):# o +1 é para contar até o número escolhido, pois sempre conta um a menos
    print(c)
print('fim')

#inici fim e passos 
i=int(input('inicio: '))
f=int(input('fim: '))
p=int(input('passo: '))

print('O boneco vai do {} até o {} pulando de {} em {} casa(s)'.format(i,f,p,p))

for c in range(i,f+1,p):
    print(c)
print('fim')