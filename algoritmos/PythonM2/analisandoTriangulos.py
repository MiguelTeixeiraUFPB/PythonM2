lado1=int(input('primeiro segmento: '))
lado2=int(input('segundo segmento: '))
lado3=int(input('terceiro segmento: '))

if lado1< lado2+lado3 and lado2< lado1+lado3 and lado3<lado1+lado2:
    print('você pode formar um triangulo', end=' ')
    
    if lado1==lado2==lado3:
        print('esse triângulo é equilatero')
    if lado1 != lado2!= lado3!= lado1:
        print('escaleno')
    if lado1==lado2!=lado3 or lado1==lado3!=lado2 or lado2==lado3!=lado1:
        print('isoceles')
