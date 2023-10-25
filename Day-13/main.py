# numbers = [5, 3, 7, 8, 9, 23, 12]  # Output [1, 4, 9, 16]
# newNumbers = []
#
# for I in numbers:
#     newNumbers.append(I * I)
#
# print(newNumbers)


# Tuple

# x = (1, 2, 3, 4)  # Tuple
# a = [1, 2, 3, 4]  # List
#
# li = []  # Empty List
# t = ()  # Empty Tuple
#
# for i in x:
#     print(i)

# numbers = (10, 20, 30, 40)
#
# n1, n2, n3, n4 = numbers
#
# print(numbers[1])

# a = {1, 2, 3, 4}
# b = {2, 4, 6, 8, 10}
# union = a | b  # Union Operation
# intersection = a & b  # Intersection Operation
# x = set()  # Empty set
#
# print(intersection)

# userInput = int(input("Enter a number: "))
# if userInput in a:
#     print('Yes')
# else:
#     print("No")

students = ['Mahofi', 'Sadia', 'Rifat', 'Mehedi']
studentsRoll = [0, 1, 2, 3]

print(studentsRoll[students.index('Sadia')])
