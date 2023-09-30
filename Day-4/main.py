# Modulus operator is a percent sign ( % )

a = 15
b = 7

result = a % b  # 17 / 7 = 2/1

"""
7 | 15 | 2
    14
-------------
    1
"""
print(result)  # 1

year = int(input("Enter Year: "))  # Get year from user input, datatype int

if year % 4 == 0:
    print("Yes")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

