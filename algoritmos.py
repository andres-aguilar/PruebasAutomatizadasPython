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
