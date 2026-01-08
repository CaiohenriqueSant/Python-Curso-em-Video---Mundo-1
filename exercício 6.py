#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = float(input('digite um numero: '))

dobro = n * 2
triplo = n * 3
raiz = n**(1/2)

print ('o dobro de {} é {}'.format(n, dobro))
print ('o triplo de {} é {}'.format(n, triplo))
print ('a raiz de {} é {}'.format(n, raiz))


