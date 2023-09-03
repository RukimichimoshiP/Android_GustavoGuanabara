num1 = float(input('Digite o primeiro segmento: '))
num2 = float(input('Digite o segundo segmento: '))
num3 = float(input('Digite o terceiro segmento: '))

if(num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2):
    print('Os segmnetos acima PODEM FORMAR um triângulo', end=' ')
    if(num1 != num2 and num1 != num3 and num2 != num3):
        print('Escaleno!')
    elif(num1 == num2 and num1 == num3 and num2 == num3):
        print('Equilátero!')
    else:
        print('Isósceles!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
