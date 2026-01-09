#Crie um programa que leia o e-mail de uma pessoa. Em seguida, mostre: O nome do usuário. O domínio do e-mail
import random

email = str(input('Digite seu e-mail: '))

arroba = email.find('@')
dominio = email[arroba + 1:].upper()
usuario = email[:arroba]

print('o seu Domínio é {}'.format(dominio))
print('O seu Usuário é {}'.format(usuario.upper()))


