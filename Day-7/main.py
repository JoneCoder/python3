# Function Or Method

# a = float(input("Enter a number: "))
# b = float(input("Enter an another number: "))
#
#
# def add(a, b):
#     return a + b
#
#
# result = add(a, b)
#
# print(result)

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


terminateProgram = False
while not terminateProgram:
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter another: "))

    while True:
        operation = input("Please enter add/sub or quit to exit: ")

        if operation == "quit":
            terminateProgram = True
            break

        if operation not in ["add", "sub"]:
            print("Unknown operation!")
            continue

        if operation == "add":
            print("Result is: ", add(number1, number2))
            break

        if operation == "sub":
            print("Result is: ", sub(number1, number2))
            break
