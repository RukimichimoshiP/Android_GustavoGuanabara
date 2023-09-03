s = ''
while s != 'M' and s != 'F':
    s = input('Digite o seu sexo: [M/F] ').upper()
if(s == 'M'):
    print('Você é do sexo Masculino!')
else:
    print('Você é do sexo Feminino!')