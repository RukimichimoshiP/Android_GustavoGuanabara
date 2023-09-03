maiores = 0
homens = 0
mulheres20 = 0

while True:
    print('-'*31)
    print('     CADASTRE UMA PESSOA     ')
    print('-'*31)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ')
    while sexo.upper() != 'M' and sexo.upper() != 'F':
        sexo = input('Sexo: [M/F] ')
    print('-'*31)
    cont = input('Quer continuar? [S/N] ')
    while cont.upper() != 'S' and cont.upper() != 'N':
         cont = input('Quer continuar? [S/N] ')
    if(idade >= 18):
        maiores += 1
    if(sexo.upper() == 'M'):
        homens += 1
    if(sexo.upper() == 'F' and idade < 20):
        mulheres20 += 1
    if(cont.upper() == 'N'):
        break
print('='*6, ' FIM DO PROGRAMA ', '='*6)
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres20} com menos de 20 anos')