# Dictionary
# marks = [78, 72, 68, 80, 63]  # Bangla subject marks
#
# roll = int(input('Please enter your roll number:'))
#
# result = marks[roll-1]
#
# print(result)

# marks = [[78, 80], [68, 69], [80, 78], [63, 73]]  # Bangla & English marks
#
# roll = int(input('Please enter your roll number:'))
#
# result = marks[roll-1]
#
# print(result)

# marks = {
#     1: 78,  # key : value
#     2: 72,
#     3: 68,
#     4: 63
#     }

# marks = {
#     101: 78,  # key : value
#     102: 72,
#     103: 68,
#     104: 63
#     }

# marks = {
#     'Riyan': 78,  # key : value
#     'Riyan2': 72,
#     'SB-03': {1: 26, 2: 35, 3: {}, 4: []},
#     (1, 2, 3): [1, 2, 3, 4]
# }
#
# roll = input('Please enter your roll number:')
#
# print(marks[roll])
#
# emptyDict = {}  # Empty Dictionary


marks = {
    'DH1001': {'Bangla': 78, 'English': 65},
    'DH1002': {'Bangla': 82, 'English': 75},
}

# print(marks['DH1001']['Bangla'])

# for item in marks:
#     print(marks[item])

for item, value in marks.items():
    for i, v in value.items():
        print(i, v)



