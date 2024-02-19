class Calculator:
    firstNumber = 0
    secondNumber = 0
    operation = ''

    # This is a constructor method
    def __init__(self, fn, sn, op):
        self.firstNumber = fn
        self.secondNumber = sn
        self.operation = op

    # This is an add method
    def add(self):
        return self.firstNumber + self.secondNumber

    # This is a subtract method
    def subtract(self):
        return self.firstNumber - self.secondNumber

    # This is a multiplication method
    def multiplication(self):
        return self.firstNumber * self.secondNumber

    # This is a calculate method
    def calculate(self):
        match self.operation:
            case '+':
                return self.add()
            case '-':
                return self.subtract()
            case '*':
                return self.multiplication()
            case _:
                return 'Unsupported operation!'
