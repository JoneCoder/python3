students = ['Mehedi', 'Mahofi', 'Riyan', 'Rifat', 'Sadia', 'Arafat', 'Rid']

# students.append('Arafat')
# students.insert(0, 'Arafat')
# students.remove('Rid')

# print(students)

fruits = ['apple', 'mango', 'coconut', 'banana', 'orange']

# userInput = input('What do you want to eat? :')
# userInput = userInput.lower()
#
# if userInput in fruits:
#     fruits.remove(userInput)
#     print(fruits)
# else:
#     print(userInput, 'not in box.')

# print(fruits.pop())

# li = []  # Empty list
# for i in range(10):
#     li.append(i)
#
# print(li)


numbers = [1, 3, 4, 5, 8, 6, 9]
numbers2 = [10, 11, 34, 26]

# print(numbers + numbers2)
# print(numbers2 * 3)

# li = ['a', 'b', 'c']
# strData = " ".join(li)
#
# print(strData)


li = [1, 3, 4, 6, 7, 9, 12, 34, 5, 6, 8, 10]
resultNumbers = []  # Define Empty list

for i in li:
    if i % 2 == 0:
        resultNumbers.append(i)

print(resultNumbers)
