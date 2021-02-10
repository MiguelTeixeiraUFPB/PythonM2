passaporte=130#valor inteiro
taxaPEF=120
taxaDNZ=180
pais=str(input('qual o país destino? ')).upper()
tipopassaporte=str(input('passaporte novo ou renovação? ')).upper()

if pais=='PORTUGAL' or pais=='ESPANHA' or pais=='FRANÇA':
    if tipopassaporte=='NOVO':
        print('o valor a ser pago é'.format(taxaPEF+passaporte))
    else:
        print('o valor a ser pago é'.format(taxaPEF+(passaporte/2))



