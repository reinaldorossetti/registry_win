#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Função para criar um Renavam aleátorio.
# Baseado no forked from ellisonleao/renavam.py, que valida um renavam, no meu caso crio.

import random


def renavam_funcional():
    """
    No caso do RENAVAM, o DV (dígito verificador) módulo 11 é calculado
    multiplicando cada dígito do número base pela sequência de multiplicadores
    2, 3, 4, 5, 6, 7, 8, 9, 2 e 3, posicionados da direita para a esquerda.
    O somatório destas multiplicações é multiplicado por 10 e depois dividido
    por 11, e o resto desta divisão é o DV.
    Porém, sempre que o resto da divisão for 10, o DV será 0.
    """
    renavam = [random.randrange(9) for i in range(11)]
    #print(renavam)

    # remove ultimo digito (verificador)
    renavam_sem_digito = renavam[:-1]

    # inverte
    renavam_sem_digito = renavam_sem_digito[::-1]

    # Multiplica as strings reversas do renavam pelos numeros multiplicadores
    # para apenas os primeiros 8 digitos de um total de 10
    # Exemplo: renavam reverso sem digito = 69488936
    # 6, 9, 4, 8, 8, 9, 3, 6
    # *  *  *  *  *  *  *  *
    # 2, 3, 4, 5, 6, 7, 8, 9 (numeros multiplicadores - sempre os mesmos [fixo])
    soma = 0
    for i, digito in enumerate(renavam_sem_digito[:8]):
        soma += int(digito) * (i + 2)

    # Multiplica os dois ultimos digitos e soma
    soma += int(renavam_sem_digito[8]) * 2
    soma += int(renavam_sem_digito[9]) * 3

    # mod11 = 284 % 11 = 9 (resto da divisao por 11)
    mod11 = soma % 11

    # Faz-se a conta 11 (valor fixo) - mod11 = 11 - 9 = 2
    ultimo_digito_calculado = 11 - mod11

    # ultimoDigito = Caso o valor calculado anteriormente seja 10 ou 11,
    # transformo ele em 0. caso contrario, eh o proprio numero
    if ultimo_digito_calculado >= 10:
        ultimo_digito_calculado = 0

    # voltando normal o invert
    renavam_sem_digito= renavam_sem_digito[::-1]

    # adicionando o ultimo digito valido.
    renavam_sem_digito.append(ultimo_digito_calculado)

    # retornando a string com os valores corretos.
    renavam_new = (''.join(str(e) for e in renavam_sem_digito))

    print(renavam_new)

    return renavam_new

renavam_funcional()
