from datetime import date
ano=int(input('digite o ano em que você nasceu: '))
anoatual=date.today().year
idade=anoatual-ano 
tempo=idade-18

if idade==18:
    print("você deve se alistar ao imediatamente")
elif idade>18:
    saldo=idade-18
    anodealistameno=saldo-anoatual
    print('você já passou {} ano(s) da idade para o alistamento, o seu ano de alistamento foi {}'.format(saldo,anodealistameno))
else:
    saldo=18-idade
    anodealistameno=ano-saldo
    print('você ainda não tem idade para se alistar, ainda faltam {} ano(s), o seu ano de alistamento será em {}'.format(saldo,anodealistameno))
print()