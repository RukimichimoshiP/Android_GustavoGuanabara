termo = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = termo + (10 - 1) * r

for c in range(termo, decimo + r, r):
    print(c, end=' -> ')
print('Acabou')
