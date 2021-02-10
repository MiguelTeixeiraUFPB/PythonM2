buenosairesdia=220
santiagodia=307
montevideodia=280.6

viagembuenosaires=810
viagemsantiago=900.50
viagemmontevideo=780

dias=int(input('quantidade de dias:'))
lugar=(input('qual lugar deseja ir:')).upper()

if lugar=='BUENOS AIRES':
    print('o valor a ser pago pela hospedagem é {}R$ e a passagem é {}R$'.format(buenosairesdia*dias,viagembuenosaires*2))
elif lugar=='MONTEVIDEO':
    print('o valor a ser pago pela hospedagem é {}R$ e a passagem é {}R$'.format(montevideodia*dias,viagemmontevideo*2))
else:
    print('o valor a ser pago pela hospedagem é {}R$ e a passagem é {}R$'.format(santiagodia*dias,viagemsantiago*2))
print()