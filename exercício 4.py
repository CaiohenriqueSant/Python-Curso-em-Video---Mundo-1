    #Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a= input('digite algo: ')

print ('o tipo primitivo desse valor é {}'.format(type(a)))
print ('só tem espaços? {}'.format(a.isspace()))
print ('é um número? {}'.format(a.isnumeric()))
print ('é alfabético? {}'.format(a.isalpha()))
print ('é alfanúmerico? {}'.format(a.isalnum()))
print ('está em maiusculas? {}'.format(a.isupper()))
print ('está em minusculas? {}'.format(a.islower()))
print ('está capitalizada? {}'.format(a.istitle()))