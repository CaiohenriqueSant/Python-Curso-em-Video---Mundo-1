#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#núemros que vão ser verificados:
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

#veriicador de qual número é menor:
menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
    
#verificador de qual número é maior:
maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if  num3 > num2 and num3> num1:
    maior = num3

#Resposta final:
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')