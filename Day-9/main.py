# Function or method

def leapYear(userInput):
    if userInput % 4 == 0:
        result = "Yes"
    elif userInput % 100 == 0:
        result = "Yes"
    elif userInput % 400 == 0:
        result = "Yes"
    else:
        result = "No"
    return result


# year = int(input("Enter Year: "))
# result = leapYear(year)

