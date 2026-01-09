#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()

primeiro = nome.split()[0]
ultima = nome.split()[-1]

print('Seu primeiro nome é {} '.format(primeiro.capitalize()))
print('Seu último nome é {} '.format(ultima.capitalize()))