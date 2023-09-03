soma = 0
cont = 0

for c in range(0, 6):
    num = int(input('Digite um número: '))
    if(num%2 == 1):
        cont += 1
        soma += num
print('A soma dos {} números impares que você digitou é {}'.format(cont, soma))
