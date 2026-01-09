#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('qual a largura da parede? '))
altura = float(input('qual a altura da parede? '))

area = largura * altura
tinta = area / 2

print('A area dessa parede é de {:.2f} e vc vai gastar {:.2f} litros de tinta pra pintar essa parede'.format(area,tinta))
