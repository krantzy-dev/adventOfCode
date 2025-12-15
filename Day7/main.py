from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)
script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'

with open(inputpath, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
    matrix = [list(line.strip()) for line in lines]



max_line = len(matrix[0])-1
max_row = len(matrix)-1

amount_splits = 0

# li = line index; ri = row index
for li in range(1,len(matrix)):
    matrix_line = matrix[li]
    for ri in range(len(matrix_line)):
        
        if matrix[li-1][ri] in ["|","S"]:

            if matrix[li][ri] in ["."]:
                matrix[li][ri] = "|"
            elif matrix[li][ri] in ["^"]:
                amount_splits += 1
                if ri < max_row:
                    matrix[li][ri-1] = "|"
                if ri > 0:
                    matrix[li][ri+1] = "|"

    

print(amount_splits)



