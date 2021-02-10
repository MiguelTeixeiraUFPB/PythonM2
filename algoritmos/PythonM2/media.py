nota1=float(input('digite sua primeira nota: '))
nota2=float(input('digite sua segundda nota: '))

media=(nota1+nota2)/2

if media>=7:
    print('o aluno foi aprovado com média igual a {:.1f}'.format(media))
elif media<=5:
    print(' o aluno foi reprovado com média igual a {:.1f}'.format(media))
elif media<7 and media>=5:
    print('o aluno foi para recuperação com média igual a {:.1f}'.format(media))
print()