#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n= int(input('digite um numero: '))
ant = n - 1
suc = n + 1
print('o numero sucessor de {} é {} e o numero antecessor é {}'.format(n, suc, ant))