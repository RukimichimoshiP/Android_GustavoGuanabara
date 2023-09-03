from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
print('------------ PEDRA - PAPEL - TESOURA ------------')
print('[ 0 ] Pedra \n [ 1 ] Papel \n [ 2 ] Tesoura')
pc = randint(0, 2)
pessoa = int(input('Selecione o seu objeto: '))

if(pessoa != 0 and pessoa != 1 and pessoa != 2):
    print('Essa opção não existe!')
    exit()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('O PC escolheu {} \n você escolheu {}'.format(itens[pc], itens[pessoa]))

if(pc == 0 and pessoa == 1 or pc == 1 and pessoa == 2 or pc == 2 and pessoa == 0):
    print('Isso foi Vitória!')
elif(pessoa == 0 and pc == 1 or pessoa == 1 and pc == 2 or pessoa == 2 and pc == 0):
    print('Isso foi Derrota!')
elif(pc == 0 and pessoa == 0 or pc == 1 and pessoa == 1 or pc == 2 and pessoa == 2):
    print('Isso foi Impate!')
