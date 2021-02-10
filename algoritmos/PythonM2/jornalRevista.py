
tipo=str(input('qual assinatura deseja assinar, revista ou jornal: ')).upper()
muraldesconto=(200*10)/100
ocoretodesconto=(235*10)/100
mural=200-muraldesconto
ocoreto=235-ocoretodesconto
meular=180
suamesa=230
if tipo== 'JORNAL':
    jornal=str(input('digite o jornal que deseja assinar: ')).upper()
    if (jornal=='MURAL'):
        print('o valor do jornal é {}R$'.format(mural))
    elif (jornal=='O CORETO' or jornal=='OCORETO'):
        print('o valor do jornal é {}R$'.format(ocoreto))
else:
    revista=str(input('digite a revista que deseja assinar: ')).upper()
    if (revista=='MEU LAR' or revista=='MEULAR'):
        print('o valor da revista é {}'.format(meular))
    else:
         print('o valor da revista é {}'.format(suamesa))
print()

    

