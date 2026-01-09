#A fábrica de móveis te deu uma lista de peças, mas o sistema está todo bagunçado. Faça um programa que: Leia o nome de uma peça, remove os espaços inúteis no começo e no fim, mostra o nome das peças todas em maiúsculas, mostrar quantas letras tem o nome das peças(sem contar os espaços . Secada pea custa 12,50, mostrar quanto custaria comprar 15 (formatado com {:.2f}
import math

nome = input('Qual o nome da peça?: ').strip().upper()
sem_espaço = nome.replace(' ','')
total_letras = len(sem_espaço)
print(total_letras)
valor = 12.50
quantidade = valor * 15
print('Se o {} vale {:.2f} para comprar 15 deles o valor fica em {:.2f}'.format(nome, valor, quantidade))




