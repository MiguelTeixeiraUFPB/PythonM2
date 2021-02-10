soma=0
contador=0
for c in range(1,11):
    num=int(input('digite o {}º valor: '.format(c)))
    if num%2==0:
        soma=soma+num
        contador=contador+1
print('a soma dos número(s) pares é {} e a quantidade de número(s) pare é {} e a quantidade de números no total é {}'.format(soma,contador,c))
