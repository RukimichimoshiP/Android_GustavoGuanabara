termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

c = 0
limite = 10
while c < limite:
    if(c == 0):
        print(termo, end=' -> ')
        termo += razao
    elif(c == limite-1):
        print(termo)
        cont = int(input('Quantos mais termos você gostaria de ver: '))
        limite += cont
    else:
        print(termo, end=' -> ')
        termo += razao
    c += 1
