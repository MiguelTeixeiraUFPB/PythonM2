soma=0
count=0

for c in range(1,501,2):
    if c%3==0 and not c%2==0:
        soma+=c
        count+=1
print('a soma dos npumeros impares divisiveis por 3 é {}'.format(soma))
print(' a quantidade de números impares divisiveis por 3 é {}'.format(count))