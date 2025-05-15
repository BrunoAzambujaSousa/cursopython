"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite aqui um número inteiro: ')

try:
    numero = int(numero)
    
    if numero % 2 == 0:
        print(f'O número é PAR')
    
    else:
        print(f'O número é IMPAR')
    
except:
    print('Não é um número inteiro')
   


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


horario = input('Que horas são? ')
horas_int = int(horario)
bom_dia = horas_int >=0 and horas_int <= 11
boa_tarde = horas_int >= 12 and horas_int <= 17
    
if  bom_dia:
    print('Bom dia!')
    
elif boa_tarde:
    print('Boa tarde!')

else:
    print('Boa noite!')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')
nome_curto = len(nome) <= 4
nome_normal = len(nome) <= 6
nome_grande = len(nome) > 6

if nome_curto:
    print('Seu nome é curto')
    
if nome_normal:
    print('Seu nome é normal')
    
if nome_grande:
    print('Seu nome é grande')