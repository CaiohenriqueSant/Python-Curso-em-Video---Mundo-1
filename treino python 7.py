#Crie um algoritímo que calcule a idade de uma pessoa com base na data de nascimento, se tiver mais que 18 está recenseado
import math
from datetime import date

data_hoje = date.today()

print(f'A data de hoje é: {data_hoje.strftime('%d/%m/%Y')}')

confirmado = False
while confirmado == False:
    dia_nasc = int(input('Digite o dia em que você nasceu: '))
    mes_nasc = int(input('Digite o mês em que você nasceu: '))
    ano_nasc = int(input('Digite o ano em que você nasceu: '))
    data_nasc = date(ano_nasc, mes_nasc, dia_nasc)
    resposta = str(input(f'O ano que você nasceu é: {data_nasc.strftime('%d/%m/%Y')}?\nDigite "Y" para SIM se sua data estiver correta ou "N" para NÃO se estiver incorreta: ')).upper()
    if resposta == 'Y':
        confirmado = True
        total_dias = (data_hoje - data_nasc).days
        idade = math.floor(total_dias / 365.25)
        print(f'Sua idade é {idade}.')
    else:
        print('Digite seus dados novamente')

if  idade >= 18:
    print('Você está recenseado.')
elif idade == 17:
    print('Você ainda não pode ser recensseado, volte ano que vem.')
else:
    print('Você ainda é muito jovem para o recensseamento.')
#ESSE DESAFIO FOI DIFICIL PRA CACETE, QUE DIACHO DE DESAFIO FOI ESSE KURIEL (COMECEI AS 18:00 E TERMINEI 20:40)

