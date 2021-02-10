idadevelho=0
s=0
f=0
for p in range(1,3):
     print('---{}º pessoa---'.format(p))
     nome=str(input('digite o {}º nome: '.format(p))).strip()
     idade=int(input('digite a idade da {}º pessoa: '.format(p)))
     peso=float(input('digite o peso da {}º pessoa: '.format(p)))
     sexo=str(input('sexo[M/F]: ')).upper().strip()
     s+=idade
     if p==1 and sexo=='M':
         idadevelho=idade
         nomevelho=nome
     elif sexo=='M' and idade>idadevelho:
         idadevelho=idade
         nomevelho=nome
     print()
     if sexo=='F' and idade<20:
         f+=1
         nomemulher=nome
media=s/2
print('o nome do homem mais velho é',nomevelho)
print('a média de idade é {}'.format(media))
print('a quantidade de mulheres com menos de 20 anos {}'.format(f))

          

