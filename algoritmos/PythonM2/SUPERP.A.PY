n=int(input('digite o primeiro termo: '))
razao=int(input('digite a razão: '))
contador=int(input('quantidade de termos: '))
while contador!=0:
        print('{}'.format(n),end='-> ')
        n = n + razao
        contador=contador-1
        
    