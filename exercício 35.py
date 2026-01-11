#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

ordem = sorted([reta1, reta2, reta3])
menor1 = ordem[0]
menor2 = ordem[1]
resto = ordem[2]

if (menor1 + menor2) > resto:
    print(f'Sim, os comprimentos: {reta1:.2f},{reta2:.2f},{reta3:.2f} podem formar um triângulo')
else:
    print(f'Não. os comprimentos: {reta1:.2f},{reta2:.2f},{reta3:.2f} NÃO podem formar um triângulo.')

#Orgulhoso de mim mesmo, pois achei meu código mais bonito que a do Professor Guanabara!