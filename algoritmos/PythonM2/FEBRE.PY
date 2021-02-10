temperatura=float(input('qual a temperatura? '))
if temperatura<37.3:
    print('paciente sem febre')
elif temperatura>=37 and temperatura<=37.8:
    print('paciente está febril')
else:
    print('paciente com febre')