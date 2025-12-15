from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)
script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'

with open(inputpath, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
    matrix = [list(line.strip()) for line in lines]


memo = {}

def check_input_line(y,x):
    print(f"x: {x}; y: {y}; value: {matrix[y][x]}")

    if (y,x) in memo:
        return memo[(y,x)]
    
    if y >= len(matrix)-1:
        return 1

    current_char = matrix[y][x]
    result = 0

    if current_char == '.':
        result = check_input_line(y+1,x)

    elif current_char == '^':
        if x == len(matrix[0])-1:
            result = check_input_line(y+1,x)
        elif x==0:
            result = check_input_line(y+1,x+1)
        else:
            result=check_input_line(y+1,x-1)+check_input_line(y+1,x+1)
    
    memo[(y,x)] = result
    return result

    

timelines = 0
for i in range(len(matrix[0])):
    if matrix[0][i] == 'S':
        timelines += check_input_line(1, i)
        break
print(timelines)