cont = True
cont2 = True

while cont:
    cont2 = True
    print('-'*15)
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    print('Oque você gostaria de fazer com eles:')
    print('[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos Números \n[5]Sair do Programa')
    while cont2:
        escolha = int(input('Digite a sua opção: '))
        if(escolha == 1):
            res = num1 + num2
            print('O resultado da sua soma foi {}'.format(res))
            cont2 = False
        elif(escolha == 2):
            res = num1 * num2
            print('O resultado da sua multiplicação foi {}'.format(res))
            cont2 = False
        elif(escolha == 3):
            if(num1 > num2):
                print('O maior número digitado foi {}'.format(num1))
            elif(num2 > num1):
                print('O maior número digitado foi {}'.format(num2))
            else:
                print('O número {} é igual ao número {}'.format(num1, num2))
            cont2 = False
        elif(escolha == 4):
            print('Escolha novos número!!!')
            cont2 = False
        elif(escolha == 5):
            cont2 = False
            cont = False
        else:
            print('Está opção não existe, escolha outra')
print('Acabou!!!')