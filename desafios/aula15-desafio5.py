total = 0
maisdemil = 0
barato_nome = ''
barato_preco = 0
i = 0

print('-'*31)
print(' '*5,'LOJA SUPER BARATÃO')
print('-'*31)

while True:
    nome = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    cont = input('Quer continuar? [S/N] ')
    while('S' not in cont.upper() and 'N' not in cont.upper()):
        cont = input('Quer continuar? [S/N] ')

    total += preco
    if(i == 0):
        barato_preco = preco
        barato_nome = nome

    if(preco >= 1000):
        maisdemil += 1
    if(preco < barato_preco):
        barato_preco = preco
        barato_nome = nome

    if('N' in cont.upper()):
        break

    i += 1
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisdemil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato_nome} que custa R${barato_preco}')