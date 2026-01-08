#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual o valor deste produto?: '))

desconto = preço - (preço * 5 / 100)

print('Este produto com 5% de desconto fica {}'.format(desconto))