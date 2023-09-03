num = int(input('Digite o primeiro termo da sequência: '))
repeticoes = int(input('Digite quantas vezes você quer repetir: '))
res = 0
res2 = 0

c = 1
while c <= repeticoes:
    if(c == 1):
        res = num-1
        print(res, end=' -> ')
        print(num, end=' -> ')
    elif(c == repeticoes):
        print(num)
    else:
        res2 = num
        num += res
        res = res2
        print(num, end=' -> ')
    c += 1