nome = 'Pai do Maurício'
altura = 1.69
peso = 72
indice = ... # IMC = peso / (altura x altura)
imc = peso / (altura * altura)

'f-strings'
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)