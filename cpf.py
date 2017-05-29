import random
"""
Primeiramente multiplica-se os 9 primeiros dígitos pela sequência decrescente de números de 10 à 2 e soma os resultados.

5 * 10 + 2 * 9 + 9 * 8 + 9 * 7 + 8 * 6 + 2 * 5 + 2 * 4 + 4 * 3 + 7 * 2
    
"""


def cpf_funcional():
    # gera uma lista de nove numeros aleatorios.
    lista_numeros= [random.randrange(10) for i in range(9)]

    # calcula digito 1 e acrescenta ao numero
    # zip vai unir duas listas
    # primeira lista do randon e a segunda eh lista invertida comencando por 10, 9 etc.
    soma = sum(x * y for x, y in zip(lista_numeros, range(10, 1, -1)))
    d1 = 11 - (soma % 11)
    if d1 >= 10:
        d1 = 0
    lista_numeros.append(d1)

    # calcula digito 2 e acrescenta ao numero
    soma2 = sum(x * y for x, y in zip(lista_numeros, range(11, 1, -1)))
    d2 = 11 - (soma2 % 11)
    if d2 >= 10:
        d2 = 0
    lista_numeros.append(d2)

    return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(lista_numeros)

print(cpf_funcional())