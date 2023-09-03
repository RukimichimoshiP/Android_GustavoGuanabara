import random
cont = 0

print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    num = int(input('Diga um valor: '))
    ip = input('Par ou Ímpar? [P/I] ')
    pc = random.randint(0, 10)
    total = num + pc

    print('-'*20)
    print(f'Você jogou {num} e o computador jogou {pc}. Total de {total} DEU', end=' ')
    if(ip.upper() == 'I'):
        if(total % 2 == 0):
            print('PAR')
            print('Você PERDEU!')
            break
        elif(total % 2 != 0):
            print('ÍMPAR')
            print('Você VENCEU!')
    elif(ip.upper() == 'P'):
        if(total % 2 == 0):
            print('PAR')
            print('Você VENCEU!')
        elif(total % 2 != 0):
            print('IMPAR')
            print('Você PERDEU!')
            break
    print('-'*20)

    
    print('Vamos jogar novamente...')
    cont += 1
print(f'GAME OVER! Você venceu {cont} vezes.')