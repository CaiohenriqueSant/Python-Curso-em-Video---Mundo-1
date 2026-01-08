#Crie um programa que leia um número real qualquer, calcule a sua raiz quadrada e, ao exibir o resultado na tela, toque um arquivo MP3 para avisar que a tarefa foi concluída.
import math
import pygame

num = float(input('digite um numero: '))
raiz = math.sqrt(num)
print ('A raiz de {} é {:.2f}'.format(num, raiz))

pygame.init()
pygame.mixer.music.load('alarme.mp3')
pygame.mixer.music.play()

input('Cálculo concluído! Ouça o alarme e aperte Enter para parar.')

