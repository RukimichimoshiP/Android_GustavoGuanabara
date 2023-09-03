termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

c = 0
while c < 10:
    if(c == 0):
        print(termo, end=' -> ')
        termo += razao
    elif(c == 9):
        print(termo)
    else:
        print(termo, end=' -> ')
        termo += razao
    c += 1