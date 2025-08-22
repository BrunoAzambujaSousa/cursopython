'''
Iterável -> str, range, etc... (método __iter__)
Iterador -> quem sabe entregar um valor por vez
next     -> me entregue o próximo valor
inter    -> me entregue seu iterador

texto = 'Bruno'.__iter__()

# jeito mais simples
texto2 = iter('Bruno')
'''
''' 
print(texto2.__next__())

print(next(texto2))
'''
texto = 'Bruno'
'''
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
'''

for letra in texto:
    print(letra)

