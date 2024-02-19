import Calculator as C

firstNumber = float(input('Enter a number:'))
secondNumber = float(input('Enter an another number:'))
op = input('What do you want?')

calculator = C.Calculator(firstNumber, secondNumber, op)  # This is a Calculator class instance
result = calculator.calculate()  # Call to calculate method

print(result)
