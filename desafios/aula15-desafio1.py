cont = s = 0

while True:
    valores = int(input('Digite um valor (999 para parar): '))
    if(valores == 999):
        break
    s += valores
    cont += 1
print(f'A soma dos {cont} valores foi {s}!')