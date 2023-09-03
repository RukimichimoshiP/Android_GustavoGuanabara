num = int(input('Digite um número inteiro: '))
print('escolha a base númerica que você gostaria de converter ele: ')
print('[1] Binário \n [2] Octal \n [3] Hexadecimal')
base = int(input('Escolha: '))
if(base == 1):
    print('O número {} convertido para binário é {}'.format(num, bin(num)[2:]))
elif(base == 2):
    print('O número {} convertido para Octal é {}'.format(num, oct(num)[2:]))
elif(base == 3):
    print('O número {} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Esta opção não existe!')