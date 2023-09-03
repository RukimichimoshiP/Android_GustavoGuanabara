num = int(input('Digite um número: '))
cont = 0

for c in range(1, num+1):
    if(num%c == 0):
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')

print('\n\033[mEste número foi divisível {} vezes'.format(cont))
if(cont == 2):
    print('\nEste número é um número primo!')
else:
    print('\nEste número não é um número primo!')