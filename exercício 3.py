#Crie um programa que leia dois números e mostre a soma entre eles.
n1 = int(input('digite um  numero: '))
n2 = int(input('digite uoutro numero: '))
#usei o int antes do input para considerar cada número um número inteiro de forma separada, assim, ao somar os números iram somar ao invés de juntar
s = n1 + n2

print('A soma entre {} e {} é igual a {}.'.format(n1, n2, s))
