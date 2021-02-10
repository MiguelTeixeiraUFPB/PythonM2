from random import randint
computador=randint(0,10)
acertou=False
palpites=0
while not acertou:
    palpites+=1
    jogador=int(input('digite um número de 0 a 10: ')) 
    if jogador==computador:
        acertou=True
        print('você acertou!')
    else:
        elif jogador<computador:
            print('você errou!')
        if computador>jogador:
            print('o número pensado é maior')   
print('a quantidade de palpites é {}'.format(palpites))