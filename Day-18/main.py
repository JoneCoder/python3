import random
colors = ['red', 'blue', 'green', 'yellow', 'sky-blue']
randomColorIndex = random.randint(0, len(colors) - 1)
attempt = 0
while True:
    try:
        userInput = input('Guess a color:')
        userColorInput = colors.index(userInput.lower())
        attempt += 1

        if randomColorIndex == userColorInput:
            print('Your guess is correct!')
            break
        else:
            print('Color dose not match!')
    except ValueError:
        print('Invalid input! try again')


print('Your attempt', attempt, ' guess the correct answer.')

