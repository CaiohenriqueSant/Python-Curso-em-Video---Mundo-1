#Crie um programa que leia o e-mail de uma pessoa. Em seguida, mostre: O nome do usuário. O domínio do e-mail
#email = str(input('Digite seu e-mail: ')).strip()

#usuario = email.split('@')[0]
#dominio = email.split('@')[1]

#print ('O nome do usuário é: {}'.format(usuario))
#print ('O domínio do e-mail é: {}'.format(dominio))

email = str(input('Digite seu e-mail: '))

arroba = email.find('@')
dominio = email[arroba + 1:].upper()
usuario = email[:arroba]

print ('o seu Domínio é {}'.format(dominio))
print ('O seu Usuário é {}'.format(usuario.upper()))


