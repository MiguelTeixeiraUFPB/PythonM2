#calculadora para números binários,octal e hexadcimal
numero=int(input('digite um número inteiro de base decimal: '))

print(''' escolha:
[1] para números binários
[2] para octal
[3] para hexadecimal''')

opção=int(input('digite sua opção para mudar a base '))

if opção==1:
    print('{} convertido para binário é : {}'.format(numero,bin(numero)[2:]))
elif opção==2:
    print('{}  convertido para octal é : {}'.format(numero,oct(numero)[2:]))
elif opção==3:
    print('{}  convertido para hexadecimal é : {}'.format(numero,hex(numero)[2:]))   
else:
    print('opção inválida')
print()    
