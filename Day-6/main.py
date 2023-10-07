# Loop & Loop (Nested Loop)

students = ["Riyan", "Rifat", "Mahofi", "Mehedi"]
marks = [80, 78, 90]

for student in students:
    print("Name: ", student)
    for mark in marks:
        print("Mark: ", mark)

saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]

for country in saarc:
    print(country)

i = 0
while i < 10:
    # if i == 3:
    #     continue
    if i == 5:
        break
    print(i)
    i += 1
    # i = i + 1


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
            print("Result is: ", number1 + number2)
            break

        if operation == "sub":
            print("Result is: ", number1 - number2)
            break

