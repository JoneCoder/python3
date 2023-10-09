# calculate tow number

def calculator(num1, num2, sing):
    if sing == 'add':
        return add(num1, num2)
    elif sing == 'sub':
        return sub(num1, num2)
    else:
        return 'Invalid sign'


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


number1 = float(input("Enter a number: "))
operator = input("Enter operator: ")
number2 = float(input("Enter an another number: "))

result = calculator(number1, number2, operator)

print(result)
