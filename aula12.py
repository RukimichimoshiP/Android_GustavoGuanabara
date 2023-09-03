nome = str(input('Qual é o seu nome? '))
if(nome == 'Gustavo'):
    print('Que nome Bonito!')
elif(nome == 'Pedro' or nome =='Maria' or nome == 'Paulo'):
    print('Seu nome é bem popular no Brasil')
elif(nome in 'Victor Renato Samuel Paulo Sandro Caua'):
    print('Você tem o nome de pessoas bem importantes para mim')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))