menor = 0
maior = 0

for c in range(0, 5):
    peso = float(input('Digite o peso: '))
    if(c == 0):
        menor = peso

    if(peso > maior):
        maior = peso
    elif(peso < menor):
        menor = peso
        
print('O maior peso digitado foi {} e o menor foi {}'.format(maior, menor))
