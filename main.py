import calculator

def main():
    a = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /): ")
    b = float(input("Введите второе число: "))

    operation_func = calculator.choose_operation(operation)

    if operation_func is None:
        print("Неизвестная операция")
        return
    
    result = operation_func(a, b)

    if result is None:
        print("Ошибка деления")
    else: 
        print(result)

if __name__ == "__main__":
    main()