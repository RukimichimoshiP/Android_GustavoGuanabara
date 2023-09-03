quant = 0
res = 0
menor = maior = 0


cont = True
while cont:
    valor = int(input('Digite um número: '))

    cont2 = True
    while cont2:
        confirmacao = input('Deseja continuar? [S/N] ')
        if(confirmacao.upper() == 'S'):
            cont = True
            cont2 = False
        elif(confirmacao.upper() == 'N'):
            cont = False
            cont2 = False
        else:
            print('Está opção não existe!')
    
    res += valor
    quant += 1

    if(menor == 0):
        menor = valor
    else:
        if(menor > valor):
            menor = valor
    if(maior < valor):
        maior = valor

print('A média entre todos os valores digitados foi {:.2f}'.format(res/quant))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
