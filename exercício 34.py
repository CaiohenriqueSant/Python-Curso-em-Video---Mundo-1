#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#Descobrir o salário do empregador:
salario_atual = float(input('Qual o seu salário?: '))

#Calculo com base no salário do empregador:
aumento_sup = salario_atual + (salario_atual * 0.10)
aumento_inf = salario_atual + (salario_atual * 0.15)

#Resposta:
if salario_atual >= 1250.00:
    print(f'Seu salário é de: R$: {aumento_sup:.2f}')
else:
    print(f'Seu salário é de: R$: {aumento_inf:.2f}')