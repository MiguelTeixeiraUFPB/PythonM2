maior=homens=mulher=0

while True:
    idade=int(input('digite a idade:'))
    sexo=''
    while sexo not in 'MF':
        sexo=str(input('sexo: ')).upper().strip()[0]
    if idade>=18:
        maior=maior+1
    if sexo=='M':
        homens=homens+1
    else: 
        mulher=mulher+1
    continuar=''
    while continuar not in 'SN' :
        continuar=str(input('quer continar [S/N] ?')).upper().strip()[0]
    if continuar=='N':
        break
print('maiores de 18{}, homens{}, mulheres{}'.format(maior,homens,mulher))