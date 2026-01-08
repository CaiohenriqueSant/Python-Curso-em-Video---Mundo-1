#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
dinheiro = float(input('quantos reais você tem na carteira?: '))

dolar = dinheiro/3.27

print ('Com {} reais, você pode comprar {:.2f} dólares'.format(dinheiro,dolar))