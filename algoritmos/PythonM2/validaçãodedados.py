sexo=str(input('digite seu sexo: ')).strip().upper()[0]#strip tira os espaços e [pega a primeira letra ]
while sexo not in 'MF':
    sexo=str(input('dados inválidos, digite seu sexo: ')).strip().upper()[0]
print('sexo {} registrado com sucesso '.format(sexo))


