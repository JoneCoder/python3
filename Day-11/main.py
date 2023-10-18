# country = "Bangladesh"
# findIndex = country.find('d')
# print(findIndex)

# text = "            this is a string.              "
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())

# name = input("Enter Your Full Name:")
# print(name.strip())

# country = "Bangladesh"
# upperCountry = country.upper()
# print(upperCountry)


# Variable
"""
1. readable   exm: name = "Hassan"
2. #+=!-*%$%@ exm: +add = 1 (X)
3. _, 1-9, or letter exm: first_name = "Sadia"
4. Camel case exm: firstName = "Sadia", Snake case exm: first_name = "Sadia", kabab case exm: first-name = "Sadia"

"""


# def checkIsVowel(x):
#     vowel = ['A', 'E', 'I', 'O', 'U']
#     x = x.upper()
#     if x in vowel:
#         return True
#     else:
#         return False
#
#
# userInput = input("Enter a letter:")
# result = checkIsVowel(userInput)
#
# if result:
#     print("The letter is vowel")
# else:
#     print("The letter is consonant")

# s = "hello world"
# print(s.capitalize())

# numberString = "1,2,3,4,5,6,7"
# print(numberString.split(','))


import turtle

name = turtle.textinput("name", "What is your name?")
name = name.lower()
if name.startswith("mr"):
    print("Hello sir, how are you?")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
    print("Hello madam, how are you?")
else:
    name = name.capitalize()
    message = "Hi " + name + "! How are you?"
    print(message)

turtle.exitonclick()


"""
Input = "Hello Test! 123 123, good"

Output
===========
HT
ellotestgood
123123
! , .

"""