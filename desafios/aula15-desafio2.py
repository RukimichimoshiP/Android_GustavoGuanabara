

while True:
    cont = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    if(n < 0):
        break
    print('-'*15)
    while cont <= 10:
        print(f'{n} x {cont} = {n*cont}')
        cont += 1
    print('-'*15)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
