# Number Guessing Game

# import random
#
# number = random.randint(1, 100)
#
# attempts = 0
#
# while True:
#     userGuess = int(input('Guess the number (between 1 and 100):'))
#     attempts += 1
#     if userGuess == number:
#         print('Yes, your guess is correct!')
#         break
#     if userGuess > number:
#         print('Incorrect! please try to guess a smaller number.')
#     else:
#         print('Incorrect! please try to guess a larger number.')
#
#
# print("Tou tried", attempts, "times to find the correct number.")


# Prime Number

userInput = int(input('Enter a number:'))

primeNumbers = []

for i in range(userInput):
    if i % 2 != 0:
        primeNumbers.append(i)

print(primeNumbers)

