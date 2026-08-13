def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
       return None
    return a / b

def choose_operation(symbol):
    if symbol == "+":
        return add
    elif symbol == "*":
        return multiply
    elif symbol == "-":
        return subtract
    elif symbol == "/":
        return divide
    return None

if __name__ == "__main__":
    print(add(2, 3))
    print(divide(10, 2))