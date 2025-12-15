from pathlib import Path
import logging
import math
logging.basicConfig(level=logging.DEBUG)
script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'

with open(inputpath, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
    problems = [line.rstrip('\n') for line in lines]

# empty matrix
matrix = [[0 for _ in range(len(problems))] for _ in range(len(problems[0]))]
# first transpose the problems matrix
for i in range(len(problems)):
    for j in range(len(problems[0])):
        matrix[j][i] = int(problems[i][j]) if problems[i][j] not in ['*','+',' ', ''] else problems[i][j]

print(matrix[:5][:5])


calculations = []
calculation = []
# clean up matrix
for a in range(len(matrix)):
    # if all elements of a are ' ' or ''
    if all(x in [' '] for x in matrix[a]):
        calculations.append(calculation)
        calculation=[]
        continue
    
    calculation.append(matrix[a])

    if a >= len(matrix)-1:
        calculations.append(calculation)
        break

total=0
for c in calculations:
    operation = '+'
    numbers = []
    for row in c:
        if row[-1] == '*':
            operation = '*'
        numbers.append(int("".join(str(x) for x in row[:-1]).strip()))
    
    if operation == '+':
        total+= sum(numbers)
    elif operation == '*':
        total+= math.prod(numbers)

print(total)        