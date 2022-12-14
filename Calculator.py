class Calculator:

    def __init__(self):
        pass

    def sum(self, a, b):
        result = a + b
        return result

    def subtract(self, a, b):
        result = a - b
        return result

    def multiply(self, a, b):
        if b > 1000000:
            return 'Слишком большая степень'
        else:
            result = a * b
            return result

    def divide(self, a, b):
        if b != 0:
            result = a / b
            return result
        else:
            return 'Деление на 0'


def calculate(a, b, operation, self=None):
    result = None

    if operation == '+':
        result = Calculator.sum(self, a, b)
    elif operation == '-':
        result = Calculator.subtract(self, a, b)
    elif operation == '/':
        result = Calculator.divide(self, a, b)
    elif operation == '*':
        result = Calculator.multiply(self, a, b)
    else:
        print('Неизвестная операция')

    return result


def ask_operation():
    message = '''
Пожалуйста, введите символ операции, которую вы хотите совершить и нажмите Enter:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение

Ваш выбор:
   '''

    operation = input(message)

    return operation



def run_calculator():
    if __name__ == "__main__":
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))

    if __name__ == "__main__":
        operation = ask_operation()

        result = calculate(a, b, operation)

        print(f'Результат вычислений: {result}')


run_calculator()
