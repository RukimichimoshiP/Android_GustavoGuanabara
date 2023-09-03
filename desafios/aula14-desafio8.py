num = 0
soma = 0

while num != 999:
    num = int(input('Digite um número: (caso queira parar digite: 999) '))
    if(num != 999):
        soma += num
print('A soma de todos esses números foi {}'.format(soma))