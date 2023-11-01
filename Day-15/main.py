# user input 2
# output two

digitOneMapping = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
}

digitTwoMapping = {
    '11': 'Eleven',
    '12': 'Twelve',
    '13': 'Thirteen',
    '14': 'Fourteen',
    '15': 'Fifteen',
    '16': 'Sixteen',
    '17': 'Seventeen',
    '18': 'Eighteen',
    '19': 'Nineteen',
}

digitTwoMapping2 = {
    '10': 'Ten',
    '20': 'Twenty',
    '30': 'Thirty',
    '40': 'Forty',
    '50': 'Fifty',
    '60': 'Sixty',
    '70': 'Seventy',
    '80': 'Eighty',
    '90': 'Ninety',
}

digitThreeMapping = {
    '00': 'one hundred'
}

userInput = input('Enter Number (0 to 100):')  # 45


def getDigitCount(data):
    return len(data)


totalDigit = getDigitCount(userInput)

if totalDigit == 1:
    print(digitOneMapping.get(userInput))  # Twenty-two

