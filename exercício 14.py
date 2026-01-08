#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('quantos graus celsius está fazendo?: '))
fahrenheit = (celsius * 1.8) + 32
print('convertendo de celsius para fahrenheit, {} graus celsius fica {} fahreheint.'.format(celsius, fahrenheit))