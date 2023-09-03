''''
frase = input('Digite uma frase: ')
frase_mod = frase.replace(' ', '')
frase_inversa = ''

for c in range(len(frase_mod), 0, -1):
    frase_inversa += frase_mod[c-1]

print('O inverso de {} é {}'.format(frase.upper(), frase_inversa.upper()))
if(frase_mod.upper() == frase_inversa.upper()):
    print('Essa frase é um Palíndromo!')
else:
    print('Essa frase não é um Palíndromo!')
'''

frase = input('Digite uma frase: ')
frase_mod = frase.replace(' ', '')
frase_inversa = frase_mod[::-1]
print('O inverso de {} é {}'.format(frase.upper(), frase_inversa.upper()))
if(frase_mod.upper() == frase_inversa.upper()):
    print('Essa frase é um Palíndromo!')
else:
    print('Essa frase não é um Palíndromo!')