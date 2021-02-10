num=int(input('digite um número: '))
totaldediv=0

for c in range(1,num+1):
    if num%c==0:
        print('\033[31m',end=' ')
        totaldediv=totaldediv+1
    else:
        print('\033[34m',end=' ')
    print(c,end=' ')
print('\no número {} foi dividido {} vezes'.format(num,totaldediv))

if totaldediv>2:
    print('o número {} não primo'.format(num))
else:
    print('o número {} é primo'.format(num))