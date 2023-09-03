from datetime import date

nascimento = int(input('Digite o ano em que você nasceu: '))
ano = date.today().year
idade = ano - nascimento

print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, ano))
if(idade < 18):
    tempo = 18 - idade
    saldo = ano + tempo
    print('Você ainda vai se alistar nas forças armadas daqui {} anos'.format(tempo))
    print('Seu alistament será em {}'.format(saldo))
elif(idade > 18):
    tempo = idade - 18
    saldo = ano - tempo
    print('Você já deveria ter se alistado nas forças armadas a {} anos atras'.format(tempo))
    print('Seu alistamento foi em {}'.format(saldo))
else:
    print('Você está a tempo de se alistar nas forças armadas')