#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

cato= float(input('digite o cateto oposto: '))
cata = float(input('digite o cateto adjacente: '))

print('A hipotenusa é {:.2f}'.format(math.hypot(cato,cata)))
