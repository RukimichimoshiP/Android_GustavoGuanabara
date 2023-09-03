media = 0
velho = 0
nome = ''
menos = 0

for c in range(0, 4):
    n = input('Digite o nome: ')
    i = int(input('Digite a idade: '))
    s = input('Digite o sexo M/F: ')
    print('-'*15)
    if(s.upper() == 'M' or s.upper() == 'F'):
        if(s.upper() == 'M' and i > velho):
            velho = i
            nome = n
        elif(s.upper() == 'F' and i < 20):
            menos += 1
        media += i
    else:
        print('Esta opção não é válida!')
        exit()

print('A média de idade do grupo é {}'.format(media/4))
print('O homem mais velho do grupo é o {} que possui {} anos'.format(nome, velho))
print('{} garota(s) do grupo possuem menos de 20 anos'.format(menos))
