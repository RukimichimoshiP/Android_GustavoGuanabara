preco = float(input('Digite o valor a ser pago: '))

print('[ 1 ] À vista (dinheiro/cheque) \n [ 2 ] À vista no cartão \n [ 3 ] Em até 2x no cartão \n [ 4 ] 3x ou maio no cartão')
pagamento = int(input('Digite a forma de pagamento: '))

if(pagamento == 1):
    pagar = preco - (preco * 10 / 100)
    print('Você escolheu à vista no dinheiro/cheque!')
    print('Sua compra de {} vai custar {:.2f}'.format(preco, pagar))
elif(pagamento == 2):
    pagar = preco - (preco * 5 / 100)
    print('Você escolheu à vista no cartão!')
    print('Sua compra de {} vai custar {:.2f}'.format(preco, pagar))
elif(pagamento == 3):
    pagar = preco / 2
    print('Sua compra será parcelada em 2x de {:.2f} sem juros!'.format(pagar))
    print('Sua compra de {} vai custar {:.2f}'.format(preco, pagar))
elif(pagamento == 4):
    vezes = int(input('Em quantas vezes: '))
    if(vezes < 3):
        print('Você pode escolher outra opção!')
        exit()
    else:
        pagar = ((preco * 20 / 100) + preco) / vezes
        print('Sua compra será parcelada em {}x de {:.2f} com juros!'.format(vezes, pagar))
        print('Sua compra de {} vais custar {:.2f}'.format(preco, preco * 20 / 100 + preco))
else:
    print('Essa opção não existe!')