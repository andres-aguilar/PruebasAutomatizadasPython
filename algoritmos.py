#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fibonacci(number):
    """ Function fibonacci
    Función para calcular la serie de Fibonacci
    """
    if number == 0: 
        return 0
    elif number == 1: 
        return 1
    else: 
        return fibonacci(number-1) + fibonacci(number-2)


def palindromo(sentence):
    """ Retorno verdadero si la sentencia es palindromo
    en caso contrario retorna falso

    sentence -- String o entero

    >>> palindromo("anita lava la tina")
    True
    >>> palindromo(12321)
    True
    >>> palindromo("test")
    False
    """

    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]