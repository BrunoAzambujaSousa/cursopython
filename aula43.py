''' senha = '123456'
senha_digitada = ''
repeticoes = 0

while senha != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    repeticoes += 1

print(repeticoes)
print('Aquele laço podia ser infinito!') '''

nome = 'Bruno'

novo_texto = ''

#Para cada letra em interável
for letra in nome:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')