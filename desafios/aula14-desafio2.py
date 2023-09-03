import random

pc = random.randint(0, 10)
cont = True
tentativas = 0

while cont:
    jogador = int(input('Tenta adivinhar o número: '))
    if(pc != jogador):
        print('Tente novamente!')
    else:
        print('Você acertou!')
        cont = False
    tentativas += 1
print('Você tentou {} vezes'.format(tentativas))