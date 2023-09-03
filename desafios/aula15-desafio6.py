print('='*20)
print(' '*5, 'BANCO CEV')
print('='*20)

valor_quant = int(input('Que valor você quer sacar? R$'))
cinquenta = vinte = dez = um = 0

while True:
    if(valor_quant >= 50):
        valor_quant -= 50
        cinquenta += 1
    elif(valor_quant >= 20):
        valor_quant -= 20
        vinte += 1
    elif(valor_quant >= 10):
        valor_quant -= 10
        dez += 1
    elif(valor_quant >= 1):
        valor_quant -= 1
        um += 1
    elif(valor_quant == 0):
        break
    else:
        print('O programa não deu certo!')
if(cinquenta > 0):
    print(f'Total de {cinquenta} cédulas de R$50')
if(vinte > 0):
    print(f'Total de {vinte} cédulas de R$20')
if(dez > 0):
    print(f'Total de {dez} cédulas de R$10')
if(um > 0):
    print(f'Total de {um} cédulas de R$1')
print('='*20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')