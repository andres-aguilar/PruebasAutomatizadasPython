from algoritmos import fibonacci, palindromo, factorial

def test_fibonacci_5():
    assert fibonacci(5) == 5


def test_palindromo_anita():
    assert palindromo("anita lava la tina")

def test_factorial_5():
    assert factorial(5) == 120