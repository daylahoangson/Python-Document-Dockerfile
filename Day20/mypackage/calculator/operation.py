#mypackage/calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"

def power(a, b):
    return a ** b

def square_root(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Invalid input"

def exponentiate(a, b):
    return a ** b