""" Calculadora com while """
while True:

    numero1 = input('Digite o primeiro número: ') 
    numero2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+-/*): ')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True: 
        break