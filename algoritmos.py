#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Tests

>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120

>>> recursivo.factorial(13)
6227020800
"""

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


class Recursivo:
    def factorial(self, number):
        if number == 0:
            return 1
        else:
            return number * self.factorial(number-1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()  # Ejecuta las pruebas implementadas en el script
    doctest.testfile("test.txt")  # Ejecuta las pruebas de un archivo esterno