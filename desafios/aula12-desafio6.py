from datetime import date

ano = date.today().year
nascimento = int(input('Digite o ano em que você nasceu: '))
idade = ano - nascimento

print('O atleta tem {} anos'.format(idade))
if(idade <= 9):
    print('Você é um nadador MIRIM!')
elif(idade <= 14 and idade < 19):
    print('Você é um nadador INFANTIL!')
elif(idade == 19):
    print('Você é um nadador JUNIOR!')
elif(idade == 20):
    print('Você é um nadador SÊNIOR!')
else:
    print('Você é um nadador MASTER!')