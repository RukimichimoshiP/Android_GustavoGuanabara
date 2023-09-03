altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso/(altura ** 2)

teste = 4/(1+1)
print(teste)

print('O seu IMC é {:.1f}'.format(float(imc)), end=' ')
if(imc < 18.5):
    print('Você está abaixo do peso!'.format(imc))
elif(imc >= 18.5 and imc < 25):
    print('Você está no peso ideal!'.format(imc))
elif(imc >= 25 and imc < 30):
    print('Você está com sobrepeso!'.format(imc))
elif(imc >= 30 and imc < 40):
    print('Você está com obesidade!'.format(imc))
else:
    print('Você está com obesidade mórbida!'.format(imc))