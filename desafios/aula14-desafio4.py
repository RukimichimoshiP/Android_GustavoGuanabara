num = int(input('Digite o número: '))
res = 1
cont = True

print(str(num) + '!', end=' = ')
while cont:
    res *= num
    if(num-1 == 0):
        print(num, end=' = ')
        cont = False
    else:
        print(num, end=' x ')
    num -= 1
print(res)
