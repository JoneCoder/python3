# Variable
name = "Hassan Mahmod"  # Data type string
age = 25  # Data type integer
gpa = 4.69  # Data type float

# print(type(gpa))
# List
students = ["Hassan Mahmod", "Mehedi Hassan", "Sadia", "Riyan", "Rifat", "Arafat"]  # Data type list string
print(students[0])  # Index

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # Data type list int
print(numbers)

studentsGpa = [2.5, 4.5, 3.5, 4.0, 5.0, 2.3, 3.4, 4.0, 5.0, 2.0]  # Data type list float
print(type(studentsGpa[0]))

print(len(studentsGpa))

saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]
print(saarc[3])

countryName = input("Enter your country Name: ")
if countryName in saarc:
    print(countryName + " in saarc")
else:
    print(countryName + " not in saarc")

mark = float(input("Enter your mark: "))

if mark >= 33 and mark <= 39:
    print("D")
else:
    print("You are fail")
