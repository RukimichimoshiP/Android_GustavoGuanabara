from datetime import date

maior = 0
menor = 0

for c in range(0, 7):
    pessoa = int(input('Digite a idade: '))
    idade = date.today().year - pessoa
    if(idade >= 18):
        maior += 1
    else:
        menor += 1

print('Das pessoas que você digitou \n{} são maiores de idade \n{} são menores de idade'.format(maior, menor))
