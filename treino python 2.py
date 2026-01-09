#Você precisa sortear quem vai operar a Lidear F400 no turno da manhã. o script deve: Ler o nome de 4 funcionários. Colocar esses nomes em uma lista. escolher um dos nomes. E exibir na tela: "O operador do dia será: [NOME]".
import random

nome1 = input("Digite o nome do primeiro Operador: ")
nome2 = input("Digite o nome do segundo Operador: ")
nome3 = input("Digite o nome do terceiro Operador: ")
nome4 = input("Digite o nome do quarto Operador: ")

lista = [nome1, nome2, nome3, nome4]
escolha = random.choice(lista)

print('O operador do dia será: {}'.format(escolha))