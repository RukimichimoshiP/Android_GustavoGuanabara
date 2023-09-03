valor = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
tempo_ano = int(input('Por quanto tempo você ira pagar: '))

tempo_mes = tempo_ano*12
valor_prestacao = valor/tempo_mes
trintaporcento = salario*30/100

print('A prestação ficou em R${:.2f} por mês'.format(valor_prestacao))
if(valor_prestacao > trintaporcento):
    print('O seu salário mensal é menor que não é compativel para a compra desta casa neste tempo!')
else:
    print('Compra aprovada!')