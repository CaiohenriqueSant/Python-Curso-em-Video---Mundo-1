#Crie um programa que leia dois números e mostre a soma entre eles.
n1 = int(input('digite um  numero: '))
n2 = int(input('digite uoutro numero: '))
#usei o int antes do input para considerar cada número um numero inteiro de forma separada, assim, ao somar os numeros iram somar ao inves de juntar
s = n1 + n2

print('A soma entre {} e {} é igual a {}.'.format(n1, n2, s))
