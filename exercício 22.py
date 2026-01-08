#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas. Quantas letras ao todo (sem considerar espaços). Quantas letras tem o primeiro nome.
nome = str(input('Digite o seu nome completo: ')).strip()

print ('Seu nome com todas as letras maiúsculas é {}'.format(nome.upper()))
print ('Seu nome como todas as letras minusculas é {}'.format(nome.lower()))

espaços = (nome.replace(' ', ''))

print ('Seu nome contem {} letras'.format(len(espaços)))

nome_lista = nome.split()
primeiro_nome = nome_lista[0]

print  ('Seu primeiro nome é {} e possui {} letras'.format(primeiro_nome,len(primeiro_nome)))