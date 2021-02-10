ingles=200
frances=170
alemao=185
matricula=120
lingua=str(input('didite o idioma q pretende estudar: ')).upper()
semanas=int(input('digite a quantidade de semanas q deseja estudar: '))


if lingua=='INGLÊS' or lingua=='INGLES':
    print('você vai estudar {} e o valor é {}R$'.format(lingua,(ingles*semanas)+matricula))
elif lingua=='FRANCÊS' or  lingua=='FRANCES':
     print('você vai estudar {} e o valor é {}R$'.format(lingua,(frances*semanas)+matricula))
else:
     print('você vai estudar {} e o valor é {}R$'.format(lingua,(alemao*semanas)+matricula))
print('Boa escolha!')