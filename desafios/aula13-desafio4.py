num = int(input('Digite o número da tabuada que você deseja: '))

for c in range(0, 11):
    s = num*c
    print(num, 'X', c, '=', s)