#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('digite um angulo qualquer: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('com o angulo de {:.2f} \no seno é {:.2f} \no cosseno é {:.2f} \ne o tangente é {:.2f}'.format(angulo, sen, cos, tan))