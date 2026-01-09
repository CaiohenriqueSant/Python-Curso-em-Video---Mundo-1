#Crie um programa que leia o e-mail de uma pessoa. Em seguida, mostre: O nome do usuário. O domínio do e-mail e identifique se o domínio for GMAIL ou não, se não for, ele criará números aleatório para o username
import random

email = str(input('Digite seu e-mail: '))

arroba = email.find('@')
dominio = email[arroba + 1:].upper()
usuario = email[:arroba].upper()

if dominio == 'GMAIL.COM':
    print('Seu usuário é: {}'.format(usuario))
else:
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    resultado = "".join(map(str, random.choices(numeros, k=4)))
    usuarionum = usuario + resultado
    print('Seu usuário é: {}'.format(usuarionum))



