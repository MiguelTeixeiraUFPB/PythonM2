from datetime import date
anoNascimento=int(input('digite o ano em que nasceu: '))
ano=date.today().year
idade=ano-anoNascimento
if idade<=9:
    print('sua categoria é mirim')
elif idade>9 and idade<=15:
    print('sua categoria é infantil')
elif idade>15 and idade<=19:
    print('sua categoria é júnior')
elif idade>19 and idade<=25:
    print('sua categoria é sênior')
else:
    print('sua categoria é master')
print()