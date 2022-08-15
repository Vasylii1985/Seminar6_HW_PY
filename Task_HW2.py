
def New_calc():
    stroka = input('Введите пример: ')
    test = list(stroka.split(' '))
    x = int(test[0])
    y = int(test[2])
    if test[1] == '+':
        result = x + y
    elif test[1] == '-':
        result = x - y
    elif test[1] == '*':
        result = x * y
    elif test[1] == '/':
        result = x / y
    return (f"Результат вычислений:{result}")


print(New_calc())