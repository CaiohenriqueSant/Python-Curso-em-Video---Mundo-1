#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.]
import random
import math

confirmado = False
while confirmado == False:
    print ('ESTOU PENSANDO EM UM NUMERO DE 0 A 5')
    escolhido = (random.randint(0, 5))
    num = int(input('que número que eu pensei? '))
    if escolhido == num:
        print(f'Parabéns!!! Você acertou, o número que a máquina pensou!!!')
    elif num < 0 or num > 5:
        print('não conheço esse número ainda, tente novamente')
    else:
        print(f'Puts, você errou, o número que máquina pensou foi {escolhido} e não no {num}, tente novamente')