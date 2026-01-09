#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
palavra = str(input('digite uma palavra: '))

primeira = palavra.upper().find('A')  + 1
ultima = palavra.upper().rfind('A') + 1

print('A palavra {} tem {} letras A \nela começa no {} caractere e termina no {} caractere'.format(palavra, palavra.upper().count('A'),primeira, ultima))


