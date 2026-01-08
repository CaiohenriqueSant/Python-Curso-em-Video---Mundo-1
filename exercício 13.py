#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o seu salário atual?: '))
aumento = salario + (salario * 15 / 100)
print('com o aumento de 15% seu salario fica {:.2f}'.format(aumento))