nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if(media < 5):
    print('Sua média foi {:.2}, Você foi reprovado'.format(media))
elif(7 > media >= 5):
    print('Sua média foi {:.2}, você esta de recuperação'.format(media))
else:
    print('Sua média foi {:.2}, você está aprovado'.format(media))