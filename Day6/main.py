from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)
script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'

with open(inputpath, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
    problems = [line.strip().split() for line in lines]


# empty matrix
matrix = [[0 for _ in range(len(problems))] for _ in range(len(problems[0]))]
# first transpose the problems matrix
for i in range(len(problems)):
    for j in range(len(problems[0])):
        matrix[j][i] = int(problems[i][j]) if problems[i][j] not in ['*','+'] else problems[i][j]

solutions = [0 for _ in range(len(matrix))]

for i in range(len(matrix)):

    if matrix[i][-1] == '+':
        solutions[i] = 0
        for j in range(len(matrix[i])-1):
            solutions[i] += matrix[i][j]
    elif matrix[i][-1] == '*':
        solutions[i] = 1
        for j in range(len(matrix[i])-1):
            solutions[i] *= matrix[i][j]
    else:
        solutions[i] = 0

    logging.debug(f"solution for problem no.{i+1}: {solutions[i]}")

solution = sum(solutions)
print(solution)